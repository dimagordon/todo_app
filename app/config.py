import os


DB_DRIVER = os.getenv('DB_DRIVER', 'postgresql')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_NAME = os.getenv('DB_NAME')


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:////dev.db'


class TestingConfig(Config):
    TESTING = True
    # in memory db
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


def get_config(prefix):
    if prefix == 'dev':
        return DevelopmentConfig
    elif prefix == 'test':
        return TestingConfig
    elif prefix == 'prod':
        return ProductionConfig
    raise Exception("Wrong config prefix")
