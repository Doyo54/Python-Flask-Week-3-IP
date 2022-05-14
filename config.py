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
    SQLALCHEMY_DATABASE_URI = 'postgres://vsqhvgrthkqxkx:81126465b8db77922272b91afa85ae46992ad2c8ff00039db63ece57f44929cd@ec2-44-196-223-128.compute-1.amazonaws.com:5432/d2vtv4k7qp233f'
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
