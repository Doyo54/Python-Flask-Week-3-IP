from flask import render_template,request,redirect,url_for,abort
from app import app
from ..models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



