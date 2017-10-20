# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 07:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('name', models.CharField(blank=True, max_length=200)),
                ('registered_user', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
