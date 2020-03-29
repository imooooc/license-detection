from django.db import models
from datetime import datetime
from users.models import User
from cars.models import Car

# Create your models here.
class UserCar(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, verbose_name=u'车辆', on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户查询表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '第{x}条记录'.format(x=self.id)