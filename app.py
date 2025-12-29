# Application factory allows multiple app instances and easier testing.

from flask import Flask
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize extensions
    db.init_app(app)

    # blueprints will be registered here later

    return app