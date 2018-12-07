# Generated by Django 2.1.2 on 2018-12-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_registry_org'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Заголовок меню')),
                ('url', models.URLField(verbose_name='Адрес ссылки')),
                ('order', models.SmallIntegerField(verbose_name='Порядок вывода')),
            ],
            options={
                'verbose_name': 'Ссылка меню',
                'verbose_name_plural': 'Ссылки меню',
            },
        ),
    ]