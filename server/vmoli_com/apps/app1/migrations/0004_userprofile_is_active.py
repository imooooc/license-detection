# Generated by Django 2.2.7 on 2020-04-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200413_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='激活状态'),
        ),
    ]