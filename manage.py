"""
encoding:utf-8
入口文件
从这里启动
"""
from flask_script import Manager
from flask_migrate import MigrateCommand
from apps import create_app


app = create_app('default')
manager = Manager(app)
manager.add_command('db', MigrateCommand)
"""
迁移数据库命令：
 python  manage.py db init  初始化迁移目录 第一步只需要一次就好
 python  manage.py db migrate  生成迁移脚本
 python  manage.py db upgrade  映射到数据库中

"""


if __name__ == "__main__":
    manager.run()
