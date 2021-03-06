from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig,config_options,ProdConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app(config_name):
# Initializing application
    app = Flask(__name__)


# Setting up configuration
    app.config.from_object(config_options[config_name])
    app.config.from_object(DevConfig)
    app.config['SECRET_KEY'] = '1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vsqhvgrthkqxkx:81126465b8db77922272b91afa85ae46992ad2c8ff00039db63ece57f44929cd@ec2-44-196-223-128.compute-1.amazonaws.com:5432/d2vtv4k7qp233f'



# Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

