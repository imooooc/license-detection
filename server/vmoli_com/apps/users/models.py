# -*- coding:utf-8 -*-
# Author: Zhu Chen
# Organization: 07 LP detection group
# Create Time: 2020/04  All rights reserved
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(models.Model):
    openid = models.CharField(max_length=100, verbose_name=u'openid', unique=True)
    stu_id = models.CharField(max_length=10, verbose_name=u'学号', default='')
    pwd = models.CharField(max_length=20, verbose_name=u'密码', null=True, blank=True)
    name = models.CharField(max_length=20, verbose_name=u'姓名', default='nobody')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'用户列表'
        verbose_name_plural = verbose_name


    # 重写str方法，否则后台管理系统出错
    def __str__(self):
        return self.name
