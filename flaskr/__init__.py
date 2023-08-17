import flaskr.models

from flask import Flask
from config import DevelopmentConfig, TestingConfig
from flaskr.extensions import db, migrate, api, jwt

from flaskr.resources.post import bp as post_bp
from flaskr.resources.comment import bp as comment_bp
from flaskr.resources.user import bp as user_bp


def create_app(testing_config=None):
    app = Flask(__name__)

    if testing_config is None:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(TestingConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    jwt.init_app(app)

    api.register_blueprint(post_bp)
    api.register_blueprint(comment_bp)
    api.register_blueprint(user_bp)

    return app
