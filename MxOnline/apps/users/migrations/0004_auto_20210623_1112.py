# Generated by Django 2.2 on 2021-06-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210622_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/head_image/%Y/%m', verbose_name='用户头像'),
        ),
    ]