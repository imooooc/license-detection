# -*- encoding:utf-8 -*-
from django.db import models
from datetime import datetime


# Create your models here.
class User(models.Model):
    openid = models.CharField(max_length=100, verbose_name=u'openid', primary_key=True )
    stu_id = models.CharField(max_length=10, verbose_name=u'学号',default='')
    pwd = models.CharField(max_length=20,verbose_name=u'密码', null=True, blank=True)
    name = models.CharField(max_length=20, verbose_name=u'姓名', default='nobody')
    create_time = models.DateTimeField(verbose_name=u'创建时间', default=datetime.now )

    class Meta:
        verbose_name = u'用户列表'
        verbose_name_plural = verbose_name


    #重写str方法，否则后台管理系统出错
    def __str__(self):
        return self.name
