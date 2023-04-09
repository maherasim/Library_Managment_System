from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .models import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import json
from werkzeug.security import generate_password_hash, check_password_hash

with open('config.json', 'r') as f:
    config = json.load(f)
    database_uri = f"mysql://{config['DB_USERNAME']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"

engine = create_engine(database_uri)
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    session = DBSession()
    user = session.query(User).filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) 
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
              
        session = DBSession()
        entry = User(name=name, email=email, password=hashed_password)
        session.add(entry)
        session.commit()
        
    return render_template('login.html')

@auth.route('/logout')


@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
