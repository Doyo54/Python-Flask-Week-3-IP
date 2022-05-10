from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)


# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app.main import views

