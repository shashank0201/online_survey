# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-18 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0005_auto_20190417_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveymodel',
            name='vote_count',
            field=models.IntegerField(default='0', editable=False),
        ),
    ]
