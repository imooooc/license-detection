# -*- coding:utf-8 -*-
# Author: Zhu Chen
# Organization: 07 LP detection group
# Create Time: 2020/04  All rights reserved

from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(models.Model):
    # 用户名
    user_name = models.CharField(max_length=20, verbose_name='用户名', blank=False, unique=True)
    # 邮箱
    email = models.EmailField(max_length=50, verbose_name='用户邮箱', default='')
    # 密码
    password = models.CharField(max_length=256, verbose_name='密码', blank=False)

    # 创建时间
    create_time = models.DateTimeField( auto_now_add=True ,verbose_name='添加时间')

    # 是否激活
    is_active = models.BooleanField(default=False, verbose_name='激活状态')

    # # 生日
    # # blank=True 前端表单中的数据可以为空
    # birday = models.DateTimeField(verbose_name='生日', null=True, blank=True)
    #
    # # 住址
    # address = models.CharField(max_length=50, verbose_name='地址', default='')
    #
    # # 电话
    # mobile = models.CharField(max_length=11, verbose_name='手机', default='')
    #
    # # 用户头像
    # image = models.ImageField(upload_to='images/%Y/%m', default='image/default.png', verbose_name='头像')

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name


class EmailVeriRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name='验证码')

    # 用户邮箱
    email = models.EmailField(max_length=50, verbose_name='用户邮箱')

    # 发送时间
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='发送时间', null=True, blank=True)

    # 过期时间
    expire_time = models.DateTimeField(null=True, verbose_name='过期时间')

    # 邮件类型
    email_type = models.CharField(choices=(('register', '注册邮件'), ('forget', '找回密码')), max_length=10, verbose_name='邮件类型')

    class Meta:
        verbose_name = '邮件验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
