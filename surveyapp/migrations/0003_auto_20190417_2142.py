# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-17 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0002_auto_20190417_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveymodel',
            name='vote_count',
            field=models.IntegerField(default='0', editable=False, max_length=255),
        ),
    ]
