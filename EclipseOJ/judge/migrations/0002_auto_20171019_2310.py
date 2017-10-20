# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='status',
        ),
        migrations.AlterField(
            model_name='submission',
            name='verdict',
            field=models.CharField(choices=[('Q', 'In queue'), ('R', 'Running'), ('WA', 'Wrong Answer'), ('CE', 'Compilation Error'), ('RE', 'Runtime Error'), ('AC', 'Accepted')], default='Q', max_length=2),
        ),
    ]