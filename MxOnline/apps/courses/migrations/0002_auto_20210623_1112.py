# Generated by Django 2.2 on 2021-06-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='media/courses/%Y%m', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='file',
            field=models.FileField(max_length=200, unique='media/course/resource/%Y/%m', upload_to='', verbose_name='下载地址'),
        ),
    ]
