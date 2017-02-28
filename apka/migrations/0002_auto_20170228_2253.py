# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-28 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apka', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booklet',
            options={'verbose_name': 'Вопросы - ответы', 'verbose_name_plural': 'Вопросы-ответы'},
        ),
        migrations.AlterModelOptions(
            name='booklets',
            options={'verbose_name': 'Буклеты', 'verbose_name_plural': 'Буклеты'},
        ),
        migrations.AlterModelOptions(
            name='classes',
            options={'verbose_name': 'Клас', 'verbose_name_plural': 'Класы(прим.КРОК 1 - Стоматология)'},
        ),
        migrations.AlterModelOptions(
            name='lang',
            options={'verbose_name': 'Язык', 'verbose_name_plural': 'Языки'},
        ),
        migrations.RemoveField(
            model_name='booklet',
            name='right',
        ),
    ]
