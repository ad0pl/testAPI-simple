from app.extensions.log import configure_logging
from app.extensions.rest import rest_api, http_status_codes

def initialize_extensions(app):

    # Logging
    configure_logging(app)

    # Flask-Restful
    #endpoint_registries = [register_zelos_endpoints]
    endpoint_registries = [ ]
    rest_api.init_app(app, endpoint_registries, http_status_codes)

    if app.config['ENV'] == 'production' and app.name != 'test':
        pass

    return app
