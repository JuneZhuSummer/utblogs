from flask import Flask
from apps.views import register_blueprints
from apps.config import config
from apps.extensions import config_extensions


def create_app(config_name):  # 到底是开发环境还是测试环境还是生产环境
    # 创建实例
    app = Flask(__name__)

    # 配置蓝本
    register_blueprints(app)
    # 让配置文件生效
    app.config.from_object(config[config_name])

    # 初始化配置
    config[config_name].init_app(app)

    # 让扩展真正生效
    config_extensions(app)

    return app
