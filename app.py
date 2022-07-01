# Flask Imports
from flask import Flask
from flask_restful import Api

# Flask SQLAlchemy.
from flask_sqlalchemy import SQLAlchemy

from flask_apispec.extension import FlaskApiSpec

# DataBase Imports
# import db
import dbPostgress as db

# Import Config.
from config import get_config

# Flask ApiSpec Imports.
from docs import initialize_docs

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

docs = FlaskApiSpec(app)
initialize_docs(docs)

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run()
