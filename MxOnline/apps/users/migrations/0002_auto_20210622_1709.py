# Generated by Django 2.2 on 2021-06-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='head_image/%Y/%m', verbose_name='用户头像'),
        ),
    ]
