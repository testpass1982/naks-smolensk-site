# Generated by Django 2.1 on 2018-12-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20181209_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eqtype',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='weldequipment',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='welder',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='weldmaterial',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='weldmaterialtype',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='weldorg',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='weldtechnology',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='weldtype',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
    ]
