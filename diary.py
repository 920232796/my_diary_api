from flask_sqlalchemy import SQLAlchemy

from app import creat_app

_date_ = "2019/1/17 0:17"
_author_ = "xing"

from flask import Flask

app = creat_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=app.config["DEBUG"], threaded=True)

