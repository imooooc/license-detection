# Generated by Django 2.2.7 on 2020-04-17 07:44

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVeriRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='用户邮箱')),
                ('send_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='发送时间')),
                ('expire_time', models.DateTimeField(null=True, verbose_name='过期时间')),
                ('email_type', models.CharField(choices=[('register', '注册邮件'), ('forget', '找回密码')], max_length=10, verbose_name='邮件类型')),
            ],
            options={
                'verbose_name': '邮件验证码',
                'verbose_name_plural': '邮件验证码',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('email', models.EmailField(default='', max_length=50, verbose_name='用户邮箱')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('is_active', models.BooleanField(default=False, verbose_name='激活状态')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户列表',
                'verbose_name_plural': '用户列表',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
