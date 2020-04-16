# -*- coding:utf-8 -*-
# Author: Zhu Chen
# Organization: 07 LP detection group
# Create Time: 2020/04  All rights reserved
from django.test import TestCase
from django.contrib.auth.hashers import make_password
# Create your tests here.
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vmoli_com.settings")  # project_name 项目名称
django.setup()

# password = '123123'
# res = make_password(password)
# print(res)

#
# from django.core.mail import send_mail
#
# to_email = ['imoocbook@163.com']
# send_mail('Subject 邮箱验证', 'Here is the message.', 'weijizhu@126.com',
#     to_email)
