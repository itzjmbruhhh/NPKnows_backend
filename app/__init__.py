from flask import Flask
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

cache = Cache()

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["30 per day"]
)

def create_app():

    app = Flask(__name__)
    app.config.from_object("app.config")

    cache.init_app(app)
    limiter.init_app(app)

    from .routes import api
    app.register_blueprint(api)

    return app