# SQLAlchemy Imports.
from sqlalchemy import Column, Integer, String

# import dbSQLite as db
import dbPostgress as db


class Joke_model(db.Base):
    """ Class Model Joke
    """
    __tablename__ = "jokes"
    id = Column(Integer, primary_key=True)
    text = Column(String(500), unique=True, nullable=False)

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return ('ID : {} Chiste: {}').format(self.id, self.text)
