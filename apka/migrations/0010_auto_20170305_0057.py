# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-04 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apka', '0009_auto_20170304_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panel',
            name='t6',
        ),
        migrations.RemoveField(
            model_name='panel',
            name='t7',
        ),
        migrations.RemoveField(
            model_name='panel',
            name='t8',
        ),
        migrations.RemoveField(
            model_name='panel',
            name='t9',
        ),
        migrations.AlterField(
            model_name='panel',
            name='t1',
            field=models.CharField(max_length=300, verbose_name='ПРосмотр'),
        ),
        migrations.AlterField(
            model_name='panel',
            name='t2',
            field=models.CharField(max_length=300, verbose_name='Скачать'),
        ),
        migrations.AlterField(
            model_name='panel',
            name='t3',
            field=models.CharField(max_length=300, verbose_name='Без тестов '),
        ),
        migrations.AlterField(
            model_name='panel',
            name='t4',
            field=models.CharField(max_length=300, verbose_name='Ошибки'),
        ),
        migrations.AlterField(
            model_name='panel',
            name='t5',
            field=models.CharField(max_length=300, verbose_name='Сохрі'),
        ),
    ]
