# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 16:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20170922_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='End_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 23, 16, 31, 41, 888497)),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='Start_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 22, 16, 31, 41, 888473)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='Date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 22, 16, 31, 41, 886900)),
        ),
        migrations.AlterField(
            model_name='logintable',
            name='Start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 22, 16, 31, 41, 887937)),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='Sub_Time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 22, 16, 31, 41, 889050)),
        ),
    ]