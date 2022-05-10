from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()
# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)
app.config['SECRET_KEY'] = '1234'


# Initializing Flask Extensions
bootstrap.init_app(app)
db.init_app(app)


from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

from app.main import views

