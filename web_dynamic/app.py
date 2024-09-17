#!/usr/bin/python3
"""
Starts a Flash Web Application
"""
import os
from model.Machine import Machine
from model.__init__ import storage
from model.User import User
from model.Person import Person
from flask_session import Session
from flask import Flask, render_template, redirect, send_from_directory, url_for, request, flash, session
# from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 


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
# login_manager.login_view = 'login'

# @app.teardown_appcontext
# def close_db(error):
#     """ Remove the current SQLAlchemy Session """
#     storage.close()

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

    person = storage.get_personBy_id(Person, session['email'])
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
            Num_tel=phone_number,
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
        person = storage.get_personBy_id(Person, email)
        print(person)
        user = storage.get(User, person.id)
        print(user)


        # Verify the password
        if person and user and user.password == password:
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

        # Render reservation page or perform reservation logic
        return render_template('reserve.html', machine=machine)

    except Exception as e:
        return f"Error retrieving machine: {e}"

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)




