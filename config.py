import os;
import random
import string


class Config(object):
    CSRF_ENABLED = True
    SECRET = ""
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    APP = None


class DevelopmentConfig(object):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = '8000'
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = '8000'
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = 'localhost'
    PORT_HOST = '8000'
    URL_MAIN = 'http://%s:%s' % (IP_HOST, PORT_HOST)

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')