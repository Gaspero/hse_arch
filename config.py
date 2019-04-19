class Config(object):
    DEBUG = False
    TESTING = False
    FLASK_DEBUG = 0
    TRAILING_SLASH = False
    SECRET_KEY = 'Secret'
    DATABASE = {'engine': 'peewee.SqliteDatabase', 'name': ':memory:'}


class ProductionConfig(Config):
    DATABASE = {'name': 'XXXXXX',
                'user': 'XXXXXX',
                'password': 'XXXXXX',  # https://hci.piterdata.ninja/confluence/pages/viewpage.action?pageId=3704397
                'host': 'team2018.piterdata.ninja',
                'port': 5432}


class DevelopmentConfig(Config):
    DATABASE = {'engine': 'peewee.SqliteDatabase', 'name': 'testing.db'}
    DEBUG = False
    FLASK_DEBUG = 1
    TRAILING_SLASH = False
    SECRET_KEY = 'Secret'


class TestingConfig(Config):
    DATABASE = {'engine': 'peewee.SqliteDatabase', 'name': ':memory:'}
    TESTING = True
