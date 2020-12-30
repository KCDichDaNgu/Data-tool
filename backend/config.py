# pylint: disable=too-few-public-methods,invalid-name,missing-docstring
import os


class BaseConfig(object):
    SECRET_KEY = 'this-really-needs-to-be-changed'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    # POSTGRESQL
    DB_USER = 'postgres'
    DB_PASSWORD = 'root'
    DB_NAME = 'gene'
    DB_HOST = 'localhost'
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        name=DB_NAME,
    )

    # SQLITE
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (os.path.join(PROJECT_ROOT, "huy.db"))

    DEBUG = True
    ERROR_404_HELP = False

    REVERSE_PROXY_SETUP = os.getenv('EXAMPLE_API_REVERSE_PROXY_SETUP', False)

    AUTHORIZATIONS = {
        'oauth2_password': {
            'type': 'oauth2',
            'flow': 'password',
            'scopes': {},
            'tokenUrl': '/auth/oauth2/token',
        },
        # TODO: implement other grant types for third-party apps
        #'oauth2_implicit': {
        #    'type': 'oauth2',
        #    'flow': 'implicit',
        #    'scopes': {},
        #    'authorizationUrl': '/auth/oauth2/authorize',
        #},
    }

    ENABLED_MODULES = (
        'auth',
        'users',
        # 'products',
        'api',
    )

    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

    SWAGGER_UI_JSONEDITOR = True
    SWAGGER_UI_OAUTH_CLIENT_ID = 'documentation'
    SWAGGER_UI_OAUTH_REALM = "Authentication for Flask-RESTplus Example server documentation"
    SWAGGER_UI_OAUTH_APP_NAME = "Flask-RESTplus Example server documentation"

    # TODO: consider if these are relevant for this project
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CSRF_ENABLED = True
    SQLALCHEMY_ECHO = True
    MONGO_URI = 'mongodb://localhost:27017/tool_nhap_lieu'

    # mongodb 
    MONGODB_DB = 'tool_nhap_lieu'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017

    IMPORT_FROM_FILE_DIR = "data/import_from_file/"


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv('EXAMPLE_API_SERVER_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('EXAMPLE_API_SERVER_SQLALCHEMY_DATABASE_URI')


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True

    # Use in-memory SQLite database for testing
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'
