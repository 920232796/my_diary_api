_date_ = "2019/1/18 20:29"
_author_ = "xing"

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from app import db

class Book(db.Model):
    """"""
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(1000))
    book_collection_id = Column(Integer, nullable=False)

    def keys(self):
        return ["id", "content", "book_collection_id"]

    def __getitem__(self, item):
        return getattr(self, item)




