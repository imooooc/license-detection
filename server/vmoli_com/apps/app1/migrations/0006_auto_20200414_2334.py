# Generated by Django 2.2.7 on 2020-04-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200414_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverirecord',
            name='email_type',
            field=models.CharField(choices=[('register', '注册邮件'), ('forget', '找回密码')], max_length=10, verbose_name='邮件类型'),
        ),
    ]