# Generated by Django 2.2.7 on 2020-04-05 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=10, unique=True, verbose_name='车牌号')),
                ('confidence', models.CharField(max_length=20, null=True, verbose_name='置信度')),
                ('p1', models.IntegerField(null=True, verbose_name='p1')),
                ('p2', models.IntegerField(null=True, verbose_name='p2')),
                ('p3', models.IntegerField(null=True, verbose_name='p3')),
                ('p4', models.IntegerField(null=True, verbose_name='p4')),
                ('brand', models.CharField(max_length=10, null=True, verbose_name='品牌')),
                ('color', models.CharField(choices=[('black', '黑色'), ('white', '白色'), ('red', '红色'), ('blue', '蓝色'), ('green', '绿色'), ('gray', '灰色'), ('yellow', '黄色'), ('brown', '棕色')], max_length=10, null=True, verbose_name='颜色')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '车辆列表',
                'verbose_name_plural': '车辆列表',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.FileField(max_length=200, upload_to='images/%Y/%m', verbose_name='资源路径')),
                ('desc', models.CharField(default='一张没有描述的图片', max_length=200, verbose_name='描述信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.Car', verbose_name='车辆')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '图片信息',
                'verbose_name_plural': '图片信息',
            },
        ),
    ]
