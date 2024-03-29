# -*- coding:utf-8 -*-
# Author: Zhu Chen 
# Organization: 07 LP detection group
# Create Time: 2020/04  All rights reserved
from django.core.mail import send_mail
from users.models import EmailVeriRecord
import random
import datetime
from vmoli_com import settings
import base64


# 随机产生验证码的函数
def random_code(length=16):
    # 随机大小写组合的验证码
    chars = 'quFDGDbtwehykjahuhufHFCUHNCWEHAFDONCJUHU'
    code = ''
    for x in range(length):
        # 随机取出一个字符
        code += random.choice(chars)
    return code


def send_email(to_email, email_type):
    """
    :param to_email: 收件人的邮箱
    :param email_type: 邮件类型 register注册或forget找回
    :return: 邮件发送结果
    """
    email = EmailVeriRecord()

    # 获取验证码
    email.code = random_code()

    # 收件人
    email.email = to_email

    # 过期时间
    email.expire_time = datetime.datetime.now() + datetime.timedelta(days=7)

    # 邮件类型
    email.email_type = email_type

    # 验证链接
    s = 'c={0}&m={1}&t={2}'.format(email.code, email.email, email.email_type)
    # 对参数进行base64编码
    eq = base64.encodebytes(s.encode('utf8'))
    verify_url = 'https://vmoli.com/u/verify-email?q={0}'.format(eq.decode())

    # 发送邮件
    subject = '尊敬的{0}用户, 您好'.format(to_email)

    # 不同邮件类型发送不同模板内容
    if email.email_type == 'register':
        # 发送html格式的内容
        html_contents = '<html><p>感谢您使用微吉珠小程序</p> ' \
                        '<p>请点击以下链接进行邮箱验证，以便开始使用您的账户：</p>' \
                        '<a href="{1}" style="display: inline-block;color:#fff;' \
                        'line-height: 40px;background-color: #1989fa;border-radius: 5px;' \
                        'text-align: center;text-decoration: none;font-size: 14px;' \
                        'padding: 1px 30px;">马上验证邮箱</a></html>'.format(to_email, verify_url)

        # 如果邮件不兼容html格式，则显示纯文本内容
        contents = '感谢您使用微吉珠小程序，请点击一下链接进行邮箱验证，以开始使用您的账户：{0}'.format(verify_url)
    else:
        html_contents = '<html><p>微吉珠：您正在进行找回密码操作</p> ' \
                        '<p>如果不是本人，请忽略此邮件，并及时修改您的密码</p>' \
                        '<a href="{1}" style="display: inline-block;color:#fff;' \
                        'line-height: 40px;background-color: #1989fa;border-radius: 5px;' \
                        'text-align: center;text-decoration: none;font-size: 14px;' \
                        'padding: 1px 30px;">是我本人操作</a></html>'.format(to_email, verify_url)
        contents = '您正在进行找回密码操作，点击此链接进行确认：{0} ; 如果不是本人，请忽略并及时修改您的密码。'.format(verify_url)
    try:
        res = send_mail(
            subject,
            contents,
            settings.EMAIL_HOST_USER,
            [to_email],
            html_message=html_contents,
        )
        if res == 1:
            # 保存邮件验证码
            email.save()
            return True
        else:
            return False
    except EmailVeriRecord as e:
        print(e)
        return False
