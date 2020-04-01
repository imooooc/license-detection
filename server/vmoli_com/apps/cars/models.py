from django.db import models
from datetime import datetime
from users.models import User


# Create your models here.
# class Car(models.Model):
#
#     license_plate = models.CharField(primary_key=True, verbose_name=u'车牌号', max_length=10)
#     brand = models.CharField(max_length=20, verbose_name=u'品牌', blank=True, null=True)
#     color = models.CharField(max_length=5, verbose_name=u'颜色', null=True)
#     create_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
#
#     class Meta:
#         verbose_name = u'车辆列表'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.license_plate

class Car(models.Model):
    licence_number = models.CharField(max_length=10, verbose_name=u'车牌号')
    brand = models.CharField(max_length=10, verbose_name=u'品牌')
    color = models.CharField(max_length=20, choices=(("black", "黑色"), ("white", "白色"), ("red", "红色")),
        verbose_name=u'颜色')
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'车辆列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.licence_number


class Image(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户', null=True, on_delete=models.SET_NULL)
    car = models.ForeignKey(Car, verbose_name=u'车辆', null=True, on_delete=models.SET_NULL)
    source = models.FileField(upload_to='images/%Y/%m', max_length=200, verbose_name=u'资源路径')
    desc = models.CharField(max_length=200, verbose_name=u'描述信息', default=u'一张没有描述的图片')
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')

    class Meta:
        verbose_name = u'图片信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.desc
