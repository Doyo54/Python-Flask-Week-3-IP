from flask import render_template,redirect,url_for, flash,request
from .forms import LoginForm,RegistrationForm
from . import auth

@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()

    # flash('Invalid username or Password')
    return render_template('auth/login.html', login_form = login_form)