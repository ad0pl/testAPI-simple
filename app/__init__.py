from flask import Flask

from api.apps.config import (
    config_options,
    Config
)

def create_app(config='develop', app_name=Config.PROJECT):
    app = Flask(app_name, static_folder=None)
    config_obj = config_options(config)
    app.config.from_object(config_obj)
    initialize_extensions(app)
    register_error_handlers(app)

    return app

__all__ = ['create_app']
