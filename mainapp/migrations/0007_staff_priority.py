# Generated by Django 2.1 on 2018-12-02 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='priority',
            field=models.SmallIntegerField(default=0),
        ),
    ]