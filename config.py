class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY='development key'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
