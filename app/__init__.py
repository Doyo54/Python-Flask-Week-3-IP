from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)


# Initializing Flask Extensions
bootstrap = Bootstrap(app)
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

from app.main import views

