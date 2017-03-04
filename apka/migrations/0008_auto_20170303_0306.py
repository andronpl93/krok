# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-03 00:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apka', '0007_bottomlang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='title',
        ),
        migrations.AddField(
            model_name='classes',
            name='eng',
            field=models.CharField(max_length=300, null=True, verbose_name='Название класа, прим. КРОК 1 - атология'),
        ),
        migrations.AddField(
            model_name='classes',
            name='rus',
            field=models.CharField(max_length=300, null=True, verbose_name='Название класа, прим. КРОК 1 - атология'),
        ),
        migrations.AddField(
            model_name='classes',
            name='ukr',
            field=models.CharField(max_length=300, null=True, verbose_name='Название класа, прим. КРОК 1 - атология'),
        ),
        migrations.AlterField(
            model_name='booklets',
            name='classes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apka.Classes'),
        ),
    ]
