# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 11:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_auto_20171002_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 11, 8, 34, 893450, tzinfo=utc)),
        ),
    ]