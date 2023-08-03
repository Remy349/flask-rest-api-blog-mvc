import flaskr.models

from flask import Flask
from config import DevelopmentConfig, TestingConfig
from flaskr.extensions import db, migrate, api

from flaskr.resources.post import bp as post_bp


def create_app(testing_config=None):
    app = Flask(__name__)

    if testing_config is None:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(TestingConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    api.register_blueprint(post_bp)

    return app
