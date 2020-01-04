"""
蓝本统一注册工厂
"""

from .main import main
from .user import user
from .posts import posts

# 蓝本配置

DEFAULT_BLUEPRINT = (
    # (蓝本,url前缀)
    (main, ''),
    (posts, '/posts'),
    (user, '/user'),
)


# 注册蓝本

def register_blueprints(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
