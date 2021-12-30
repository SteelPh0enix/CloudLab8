import os

from flask import Flask
from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    
    app.config.from_mapping(
        SECRET_KEY='This is my secret key, not so secret anymore',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import calculator
    app.register_blueprint(calculator.bp)

    return app