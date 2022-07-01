# Flask Imports
from flask import Flask
from flask_restful import Api

# Flask SQLAlchemy.
from flask_sqlalchemy import SQLAlchemy

# DataBase Imports
# import db
import dbPostgress as db

from config import get_config
# Imports Routes.
from resources.routes import initialize_routes


# App Instance.
# * If you need test app, you need send "env" in "get_config" fuction
env = 'test'
app = Flask(__name__)
app.config.from_object(get_config())

# API Config.
api = Api(app)
initialize_routes(api)

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run()
