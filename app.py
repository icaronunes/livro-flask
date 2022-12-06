# -*- coding: utf-8 -*-
from flask import Flask
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy

config = app_config[app_active]
db = SQLAlchemy(config.APP)

def create_app(config_name):
    app = Flask(__name__, template_folder='templates') 
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATEBASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return 'hello World'

    return app
