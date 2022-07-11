# SQLAlchemy Imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import get_config

# * If you need test app, you need send "test" in "get_config" fuction
env = 'test'
engine = create_engine(get_config().SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
