_date_ = "2019/1/18 14:59"
_author_ = "xing"


from flask import Blueprint

#这个就是这个web模块的蓝图！！
web = Blueprint("web", __name__)

## 必须导入执行一下 book中代码才会运行！
from app.web import book
