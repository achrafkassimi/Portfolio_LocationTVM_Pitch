#!/usr/bin/python3
"""
Starts a Flash Web Application
"""
import os
from model.Customer import Customer
from model.Machine import Machine
from model.Reservation import Reservation
from model.__init__ import storage
from model.User import User
from model.Person import Person
from flask_session import Session
from flask import Flask, make_response, render_template, redirect, send_from_directory, url_for, request, flash, session
from flask_login import LoginManager 
from flask import send_file, render_template_string
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from flask import make_response, render_template


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'text_only_transcript'
# Path to the upload folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure the 'uploads' folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit max upload size to 16 MB
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
Session(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)

# Check if file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # return User.query.get(int(user_id))
    return storage.get(User, user_id)

# Route: Home page (only accessible if logged in)
@app.route('/')
def home():

    machines_by_type = storage.get_machine_all()

    if "email" not in session:
        return render_template('index.html', machines=machines_by_type)

    person = storage.get_personBy_id(User, session['email'])
    print(person)
    # user = storage.get(User, person.id)
    # print(user)

    return render_template('index.html', machines=machines_by_type, person=person)

# Route: Register new users
@app.route('/register', methods=['GET', 'POST'])
def register():

    if "email" in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Retrieve form data
        file = request.files.get('image_path')
        # print(file)
        filename = None
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        username = request.form.get('username')
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone_number = request.form.get('phone_number')
        cin = request.form.get('cin')
        address = request.form.get('address')
        city = request.form.get('city')
        gender = request.form.get('gender')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            error = 'Passwords do not match!', 'danger'
            flash('Passwords do not match!', 'danger')
            return render_template('register.html', error = error)

        # Check if the email already exists
        user = storage.get(User, email)

        if user:
            error = 'Email address already exists'
            # return redirect(url_for('register'))
            return render_template('register.html', error = error)

        # Create a new user
        new_user = User(
            image_path = filename,
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            num_tel=phone_number,
            cin=cin,
            address=address,
            city=city,
            gender=gender,
            password=password
        )
        # Add user to the database
        try:
            storage.new(new_user)
            storage.save()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            error = f'An error occurred: {str(e)}', 'danger'
            return render_template('register.html', error = error)


    return render_template('register.html')

# Route: Login user
@app.route('/login', methods=['GET', 'POST'])
def login():

    if "email" in session:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # print(email, password)

        # Check if the user exists
        person = storage.get_personBy_id(User, email)
        print(person)


        # Verify the password
        if person and person.password == password:
            # login_user(user)
            
            # Store user info in Flask-Session
            session['logged_in'] = True
            session['email'] = person.email
            # print(session)
            flash('You have successfully logged in.', 'success')
            # print('Login successful!')
            return redirect(url_for('home'))
        else:
            error = 'Invalid email or password. Please try again.'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

# Route: Logout user
@app.route('/logout')
def logout():
    # Clear the session when the user logs out
    session.pop('email',None)
    session.clear()

    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/reserve/<string:machine_id>')
def reserve(machine_id):
    try:
        # Fetch the machine by ID
        # machine = session.query(Machine).get(machine_id)

        machine = storage.get(Machine, machine_id)
        if not machine:
            return "Machine not found", 404
        
        if "email" not in session:
            return render_template('reserve.html', machine=machine)
        
        person = storage.get_personBy_id(Person, session['email'])
        
        # Render reservation page or perform reservation logic
        return render_template('reserve.html', machine=machine, person=person)

    except Exception as e:
        return f"Error retrieving machine: {e}"

@app.route('/reserve_action/<string:machine_id>', methods=['POST'])
def reserve_action(machine_id):

    # machine = storage.get(Machine, machine_id)

    # If user is authenticated, use their ID
    if "email" in session:
        person = storage.get_personBy_id(User, session['email'])
        # user = storage.get(User, person.id)
        user_id = person.id
    else:
        # User not authenticated, create a new user from the form input
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')
        id_number = request.form.get('id_number')
        address = request.form.get('address')
        city = request.form.get('city')
        email = request.form.get('email')
        gender = request.form.get('gender')
        # print(gender)

        # # Check if a user already exists with this email or id_number
        # existing_user = User.query.filter_by(email=email).first()
        # if existing_user:
        #     flash('User already exists with this email. Please login.')
        #     return redirect(url_for('login'))

        # Create new customer
        new_customer = Customer(first_name=first_name, last_name=last_name, num_tel=phone, 
                        cin=id_number, address=address, city=city, email=email, gender=gender)

        storage.new(new_customer)
        storage.save()


        # Assign new user_id after creation
        user_id = new_customer.id

    # Retrieve additional reservation details from the form
    days = request.form['days']
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    prix = int(days)*70

    # Create a new reservation entry
    new_reservation = Reservation(person_id=user_id, machine_id=machine_id,
                                  start_date=start_date, end_date=end_date, prix=prix)
    
    storage.new(new_reservation)
    storage.save()

    flash('Reservation successful!')
    return redirect(url_for('reservation_success', reservation_id=new_reservation.id))

@app.route('/reservation_success/<string:reservation_id>', methods=['GET'])
def reservation_success(reservation_id):
    # Fetch the reservation details, including the machine and user information
    reaved = storage.get(Reservation, reservation_id)
    # print(reaved)
    # reservation = Reservation.query.get_or_404(reservation_id)
    machine = storage.get(Machine, reaved.machine_id)  # Assuming relationship exists between Reservation and Machine
    # print(machine)
    user = storage.get(Person, reaved.person_id)  # Assuming relationship exists between Reservation and User
    # print(user)

    # Render the reservation success template with reservation, machine, and user details
    return render_template('reservation_success.html', reservation=reaved, machine=machine, user=user)

@app.route('/generate_pdf/<string:reservation_id>', methods=['GET'])
def generate_pdf(reservation_id):
    # Fetch the reservation details, including the machine and user information
    reaved = storage.get(Reservation, reservation_id)
    machine = storage.get(Machine, reaved.machine_id)  # Assuming relationship exists between Reservation and Machine
    user = storage.get(Person, reaved.person_id)  # Assuming relationship exists between Reservation and User

    # Create the PDF in memory
    pdf_file = BytesIO()
    pdf = canvas.Canvas(pdf_file, pagesize=A4)

    # Add some text to the PDF
    pdf.drawString(100, 800, f"Reçu de Réservation: {reservation_id}")
    pdf.drawString(100, 780, f"Nom du Client: {user.first_name} {user.last_name}")
    pdf.drawString(100, 760, f"Machine Réservée: {(machine.model)}")
    pdf.drawString(100, 740, f"Date de Début: {reaved.start_date.strftime('%d/%m/%Y')}")
    pdf.drawString(100, 720, f"Date de Fin: {reaved.end_date.strftime('%d/%m/%Y')}")
    pdf.drawString(100, 700, f"prix Total : {reaved.prix}")

    pdf.showPage()
    pdf.save()

    # Send the PDF to the user as a downloadable file
    response = make_response(pdf_file.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename="reservation_receipt.pdf"'

    return response

@app.route('/faq')
def faq():
    if "email" not in session:
        return render_template('faq.html')
    
    person = storage.get_personBy_id(User, session['email'])
    # print(person)
    return render_template('faq.html', person=person)

@app.route('/product_all')
def product_all():

    machines_by_type = storage.get_all_machine()
    print(machines_by_type)

    if "email" not in session:
        return render_template('machine_list.html', machines=machines_by_type)
    
    person = storage.get_personBy_id(User, session['email'])

    return render_template('machine_list.html', person=person, machines=machines_by_type)

@app.route('/contact')
def contact():
    if "email" not in session:
        return render_template('contact.html')
    
    person = storage.get_personBy_id(User, session['email'])
    print(person)
    return render_template('contact.html', person=person)

@app.route('/rates')
def rates():
    if "email" not in session:
        return render_template('rates.html')
    
    person = storage.get_personBy_id(User, session['email'])
    print(person)
    return render_template('rates.html', person=person)

@app.route('/about')
def about():
    if "email" not in session:
        return render_template('about.html')
    
    person = storage.get_personBy_id(User, session['email'])
    print(person)
    return render_template('about.html', person=person)


if __name__ == '__main__':
    app.run(debug=True)