# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-18 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0007_surveymodel_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveymodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='surveymodel',
            name='content_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]