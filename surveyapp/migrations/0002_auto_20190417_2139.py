# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-17 21:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveymodel',
            old_name='count',
            new_name='vote_count',
        ),
    ]
