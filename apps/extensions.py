"""
导入扩展包
并实例化、初始化
"""

from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
migrate = Migrate(db=db)
moment = Moment()
# 让扩展初始化   也就是 跟app绑定
login_manager = LoginManager()


def config_extensions(app):
    moment.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'user.login'

    login_manager.login_message = '登录以后方可访问'

    # 对session的保护级别   strong 强保护   basic 一般的保护
    login_manager.session_protection = 'strong'
