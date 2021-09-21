from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'DFC8713DF4E971D3FCFDF363121C5'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app