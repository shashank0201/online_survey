# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-17 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0004_surveymodel_content_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveymodel',
            name='content_id',
            field=models.CharField(max_length=255),
        ),
    ]
