from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)# 创建flask实例
    app.config.from_object(config[config_name])# 配置信息
    config[config_name].init_app(app)# 配置信息 可能 的初始化信息
    # 其他用到的插件初始化
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    #注册蓝本
    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app