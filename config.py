from decouple import config
from flask import Flask

from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes


class DevelopmentConfig:
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}")


class TestingConfig:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@" \
                              f"localhost:{config('DB_PORT')}/{config('TEST_DB_NAME')}"


def create_app(configuration="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(configuration)

    api = Api(app)
    migrate = Migrate(app, db)
    [api.add_resource(*route) for route in routes]
    return app
