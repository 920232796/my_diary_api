from flask import Flask
from flask_sqlalchemy import SQLAlchemy

_date_ = "2019/1/18 14:59"
_author_ = "xing"

db = SQLAlchemy()

def creat_app():
    """"""
    # __name__ 标识唯一的核心对象
    app = Flask(__name__)
    app.config.from_object("app.secure")
    app.config.from_object("app.settings")
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    """"""
    from app.web.book import  web
    ##蓝图注册到app上
    app.register_blueprint(web)