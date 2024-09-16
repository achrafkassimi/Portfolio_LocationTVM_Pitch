#!/usr/bin/python3
""" Starts a Flash Web Application """

from model.__init__ import storage
from model.user import User
# The Session instance is not used for direct access, you should always use flask.session
from flask_session import Session
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
# from model.engine.db_storage import DBStorage


# storage = DBStorage()
# storage.reload()

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'text_only_transcript'
Session(app)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = 'login'

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

# # User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # return User.query.get(int(user_id))
    return storage.get_user(User, user_id)


# Route: Home page (only accessible if logged in)
@app.route('/')
def home():
    if "email" not in session:
        return render_template('index.html')
    
    user = storage.get_user(User, session['email'])
    return render_template('index.html', user=user)

# Route: Register new users
@app.route('/register', methods=['GET', 'POST'])
def register():

    if "email" in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form['email']
        username = request.form['full_name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            error = 'Passwords do not match!', 'danger'
            # return redirect(url_for('register'))
            return render_template('register.html', error=error)
        

        # Check if the email already exists
        user = storage.get_user(User, email)

        if user:
            error = 'Email address already exists'
            # return redirect(url_for('register'))
            return render_template('register.html', error=error)

        # Create a new user and add to the database
        new_user = User(email=email, username=username, password=password)
        storage.new(new_user)
        storage.save()

        print('Registration successful! Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')

# Route: Login user
@app.route('/login', methods=['GET', 'POST'])
def login():

    if "email" in session:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email, password)

        # Check if the user exists
        user = storage.get_user(User, email) # you need to fix ths function == is
        # print(type(user))

        # Verify the password
        # if user and check_password_hash(user.password, password):
        if user and user.password == password:
            # login_user(user)
            
            # Store user info in Flask-Session
            session['logged_in'] = True
            session['email'] = user.email
            # print(session)

            print('Login successful!')
            return redirect(url_for('home'))
        else:
            error = 'Invalid email or password. Please try again.'
            print('Invalid email or password. Please try again.')
            return render_template('login.html', error=error)
    
    return render_template('login.html')

# Route: Logout user
@app.route('/logout') # @login_required
def logout():
    # Clear the session when the user logs out
    session.pop('email',None)
    session.clear()

    # session['user_id'] = None
    # session['username'] = None

    # logout_user()
    print('You have been logged out.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)




