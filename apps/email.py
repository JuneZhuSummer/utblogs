"""
发送邮件方法
"""

from flask_mail import Message  # 你要发给谁 什么内容在这里构建
from flask import render_template
from flask import current_app
from apps.extensions import mail  # 发出去需要mail对象的send方法


# pop3 邮件接收服务器  110   http  80   https 443  ssh 22
# smtp 邮件发送服务器   25
# 可以通过  QQ邮箱  163邮箱  阿里云邮箱都可以
def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()  # 获取当前的app实例
    # 创建邮件信息对象
    msg = Message(subject=subject, recipients=[to], sender=app.config['MAIL_USERNAME'])
    # 如果用户用浏览器打开 显示的内容
    msg.html = render_template(template + '.html', **kwargs)
    # 如果用终端打开 显示的内容
    msg.body = render_template(template + '.txt', **kwargs)
    # 发送出去
    mail.send(message=msg)

    return '邮件已经发送'
