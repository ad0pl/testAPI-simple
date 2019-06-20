import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Set environment variables if configuration.env exists.
config_path = os.path.join(basedir, 'app/config.env')

# Assert environment configuration file exists
assert os.path.exists(config_path), 'config.env required.'
for line in open(config_path):
    var = line.strip().split('=')
    if len(var) == 2:
        os.environ[var[0]] = var[1].replace("\"", "")

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET_KEY_ENV_VAR_NOT_SET'
    PROJECT = "Centro"
    BASE_DIR = basedir
    API_TOKEN = os.environ.get('CENTRO_API_TOKEN')
class DevelopmentConfig(Config):

    # Flask
    ENV = 'development'
    DEBUG = True

    # Logging - https://docs.python.org/2/library/logging.html
    LOG_FILE = os.path.abspath(os.path.join(Config.BASE_DIR + '/logs/apps.log'))
class TestingConfig(Config):
    # Flask
    ENV = 'testing'
    DEBUG = True
    TESTING = True

    # Logging - https://docs.python.org/2/library/logging.html
    LOG_FILE = os.path.abspath(os.path.join(Config.BASE_DIR + '/logs/apps.log'))

class StagingConfig(Config):
    # Flask
    ENV = 'staging'

    # Logging - https://docs.python.org/2/library/logging.html
    LOG_FILE = '/var/log/api.log'

class ProductionConfig(Config):
    # Flask
    ENV = 'production'

    # Logging - https://docs.python.org/2/library/logging.html
    LOG_FILE = '/var/log/api.log'

def config_options(option):
    # Validate configuration option.
    if option not in ('develop', 'test', 'stage', 'prod'):
        raise NotImplementedError("Invalid configuration choice. Options include ('base', 'develop', 'test', 'prod')")

    return {
        'develop': DevelopmentConfig,
        'test': TestingConfig,
        'stage': StagingConfig,
        'prod': ProductionConfig,
    }[option]

