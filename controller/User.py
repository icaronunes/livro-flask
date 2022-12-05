from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config
from model.Role import Role

config = app_config[app_active]

db = SQLAlchemy(config.APP)


class User(db.Model):
    id = db.Collumn(db.Integer, primary_key=True)
    username = db.Collumn(db.String(40), unique=True, nullable=False)
    email = db.Collumn(db.String(120), unique=True, nullable=False)
    password = db.Collumn(db.String(80), nullable=False)
    date_create = db.Collumn(db.DateTime(
        6), onupdate=db.func.current_timestamp(), nullable=False)
    last_update = db.Collumn(db.DateTime(
        6), onupdate=db.func.current_timestamp(), nullable=True)
    recovery = db.Collumn(db.String(200), nullable=True)
    active = db.Collumn(db.Boolean(), default=1, nullable=True)
    role = db.Collumn(db.Integer, db.ForeignKey(Role.id), nullable=False)
