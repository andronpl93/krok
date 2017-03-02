# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-02 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booklet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('reply_1', models.CharField(max_length=400, verbose_name='Отввет_1')),
                ('reply_2', models.CharField(max_length=400, verbose_name='Отввет_2')),
                ('reply_3', models.CharField(max_length=400, verbose_name='Отввет_3')),
                ('reply_4', models.CharField(max_length=400, verbose_name='Отввет_4')),
                ('reply_5', models.CharField(max_length=400, verbose_name='Отввет_5')),
            ],
            options={
                'verbose_name': 'Вопросы - ответы',
                'verbose_name_plural': 'Вопросы-ответы',
            },
        ),
        migrations.CreateModel(
            name='Booklets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название буклета, прим. Буклет 2016 року')),
            ],
            options={
                'verbose_name': 'Буклеты',
                'verbose_name_plural': 'Буклеты',
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название класа, прим. КРОК 1 - Стоматология')),
            ],
            options={
                'verbose_name': 'Клас',
                'verbose_name_plural': 'Класы(прим.КРОК 1 - Стоматология)',
            },
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='прим. Українською мовою')),
                ('img', models.CharField(max_length=100, null=True, verbose_name='сылка на картинку')),
                ('code', models.CharField(max_length=100, null=True, verbose_name='Сокращенное название языка')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.AddField(
            model_name='classes',
            name='lang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='apka.Lang'),
        ),
        migrations.AddField(
            model_name='booklets',
            name='classes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apka.Classes'),
        ),
        migrations.AddField(
            model_name='booklets',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apka.Lang'),
        ),
        migrations.AddField(
            model_name='booklet',
            name='booklet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apka.Booklets'),
        ),
    ]
