# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-18 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0009_auto_20190418_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveymodel',
            name='year',
            field=models.IntegerField(),
        ),
    ]
