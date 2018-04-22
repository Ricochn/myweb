from flask import Blueprint


# 定义蓝本
main = Blueprint('main', __name__)
# 写在最后以防止循环引用
from . import views, errors