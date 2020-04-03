# Generated by Django 2.2.7 on 2020-04-01 12:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car', verbose_name='车辆')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户查询表',
                'verbose_name_plural': '用户查询表',
            },
        ),
    ]