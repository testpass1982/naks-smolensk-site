# Generated by Django 2.0.2 on 2018-11-13 09:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20181113_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish_on_main_page',
            field=models.BooleanField(default='False', verbose_name='Опубликовать на главной'),
        ),
        migrations.AddField(
            model_name='post',
            name='publish_on_main_page',
            field=models.BooleanField(default='False', verbose_name='Опубликовать на главной'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc', 'jpg', 'jpeg'], message='Something goes wrong...')], verbose_name='Документ'),
        ),
    ]
