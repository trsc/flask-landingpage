class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY='development key'
    LANGUAGES = {
        'en': 'English',
        'de': 'Deutsch'
    }

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
