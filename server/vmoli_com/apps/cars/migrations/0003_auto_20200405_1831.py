# Generated by Django 2.2.7 on 2020-04-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200405_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='confidence',
            field=models.CharField(max_length=20, null=True, verbose_name='置信度'),
        ),
    ]
