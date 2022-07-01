from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


class Config(object):
    """Config
    Base Config Model
    """
    DEBUG = False
    TESTING = False
    # SQLAlchemy

    # Silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APISPEC_SPEC = APISpec(
        title='JokeAndMath',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    )
    APISPEC_SWAGGER_URL = '/swagger/'
    APISPEC_SWAGGER_UI_URL = '/swagger-ui/'


class DevelopmentConfig(Config):
    """Development Config
    Development Config Model
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/flasksql'


class TestConfig(Config):
    """Test Config
    Test Config Model
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/test'


class ProductionConfig(Config):
    """Production Config
    Production Config Model
    """
    # production config
    pass


def get_config(env=None):
    """Get Config
    This fuction set a config mode of the app

    Args:
        env (str, optional): Type of config. Defaults to None.

    """
    if env == 'production':
        return ProductionConfig()
    elif env == 'test':
        return TestConfig()

    return DevelopmentConfig()
