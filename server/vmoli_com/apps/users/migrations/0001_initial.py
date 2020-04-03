# Generated by Django 2.2.7 on 2020-04-01 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=100, unique=True, verbose_name='openid')),
                ('stu_id', models.CharField(default='', max_length=10, verbose_name='学号')),
                ('pwd', models.CharField(blank=True, max_length=20, null=True, verbose_name='密码')),
                ('name', models.CharField(default='nobody', max_length=20, verbose_name='姓名')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户列表',
                'verbose_name_plural': '用户列表',
            },
        ),
    ]