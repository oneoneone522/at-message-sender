from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.string(150), unique = True, nullable = False)
    password = db.Column(db.string(150), unique = True, nullable = False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        if User.query.filter_by(email = email).first():
            print('Email is already registered')
            return redirect(url_for('register'))
        
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print('Account created successfully! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            print('Logged in succesfully!')
            return redirect(url_for('index'))
        else:
            print('Logged in unseccessfully. Please check email and password!')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    print('You have been logged out.')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return f"Hello, {current_user.email}! Welcome to your dashboard."
        
