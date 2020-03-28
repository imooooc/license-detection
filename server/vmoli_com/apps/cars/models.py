from django.db import models
from datetime import datetime
from users.models import User

# Create your models here.
class Car(models.Model):
    license_plate = models.CharField(primary_key=True, verbose_name=u'车牌号', max_length=10)
    brand = models.CharField(max_length=20, verbose_name=u'品牌', blank=True, null=True)
    color = models.CharField(max_length=5, verbose_name=u'颜色', null=True)
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'车辆'
        verbose_name_plural = verbose_name

# class Video(models.Model):
#     user = models.ForeignKey(User, verbose_name=u'用户', null=False)
#     car = models.ForeignKey(Car, verbose_name=u'车辆', null=True, blank=True)
#     url = models.CharField(max_length=200, verbose_name=u'资源路径', default='')
#     desc = models.CharField(max_length=200, verbose_name=u'描述信息', default='')
#     create_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

class Image(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户', null=False, on_delete=None)
    car = models.ForeignKey(Car, verbose_name=u'车辆', null=True, blank=True, on_delete=None)
    url = models.CharField(max_length=200, verbose_name=u'资源路径', default='')
    desc = models.CharField(max_length=200, verbose_name=u'描述信息', default='')
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'图片'
        verbose_name_plural = verbose_name