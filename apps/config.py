"""
数据库与邮件发送配置
"""

import os

# apps目录作为程序的主目录
base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 防止跨站请求伪造
    SECRET_KEY = 'asdfghjklzxcvbnm123'

    # 配置数据库
    # ORM模型
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置邮箱
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USERNAME = '1742092335@qq.com'
    MAIL_PASSWORD = 'kdwjpbssihbkdgdi'  # 不是邮箱的密码 而是邮箱的授权码，需要邮箱开启smtp和pop3服务

    # 使用本地bootstrap文件

    BOOTSTRAP_SERVE_LOCAL = True

    # 上传文件配置

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(base_dir,'bbs_dev.sqlite')
    DB_USERNAME = 'root'
    DB_PASSWORD = '123456'
    DB_HOST = '127.0.0.1'
    DB_PORT = '3306'
    DB_NAME = 'utblogs'
    # pip install pymysql
    DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

    SQLALCHEMY_DATABASE_URI = DB_URI


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'bbs_test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'bbs_production.sqlite')


config = {
    'develop': DevelopmentConfig,
    'text': TestConfig,
    'product': ProductionConfig,
    'default': DevelopmentConfig
}
