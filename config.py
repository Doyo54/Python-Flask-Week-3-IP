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
    SQLALCHEMY_DATABASE_URI = 'postgres://pxvpooqgwrgihu:09288300ba661ffc843ca2d5deea48b14c7a7b4c5359f5488220686f11239d34@ec2-34-227-120-79.compute-1.amazonaws.com:5432/dei07hbrpr3qsn'
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
