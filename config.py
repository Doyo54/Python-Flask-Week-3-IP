import os
import psycopg2
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://doyo:doyo123@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='1234'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI, sslmode='require')


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
