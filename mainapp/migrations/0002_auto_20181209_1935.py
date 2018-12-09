# Generated by Django 2.1 on 2018-12-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eqtype',
            name='uid',
            field=models.IntegerField(blank=True, unique=True, verbose_name='UID'),
        ),
        migrations.AlterField(
            model_name='weldequipment',
            name='uid',
            field=models.IntegerField(blank=True, unique=True, verbose_name='UID'),
        ),
        migrations.AlterField(
            model_name='welder',
            name='uid',
            field=models.IntegerField(blank=True, unique=True, verbose_name='UID'),
        ),
        migrations.AlterField(
            model_name='weldmaterial',
            name='uid',
            field=models.IntegerField(blank=True, unique=True, verbose_name='UID'),
        ),
        migrations.AlterField(
            model_name='weldmaterialtype',
            name='uid',
            field=models.IntegerField(blank=True, unique=True, verbose_name='UID'),
        ),
        migrations.AlterField(
            model_name='weldorg',
            name='uid',
            field=models.IntegerField(blank=True, unique=True, verbose_name='UID'),
        ),
        migrations.AlterField(
            model_name='weldtechnology',
            name='uid',
            field=models.IntegerField(blank=True, unique=True, verbose_name='UID'),
        ),
        migrations.AlterField(
            model_name='weldtype',
            name='uid',
            field=models.IntegerField(blank=True, unique=True, verbose_name='UID'),
        ),
    ]
