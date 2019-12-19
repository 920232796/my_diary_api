_date_ = "2019/1/22 18:01"
_author_ = "xing"

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from app import db

class BookCollection(db.Model):
    """"""
    __tablename__ = 'BookCollection'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30),nullable=False)


    def keys(self):
        return ["id", "name"]

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return "<{}, {}>".format(self.id,self.name)
