from flask import Flask
from flask_caching import Cache

cache = Cache()

def create_app():

    app = Flask(__name__)
    app.config.from_object("app.config")

    cache.init_app(app)

    from .routes import api
    app.register_blueprint(api)

    return app