# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-16 14:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yagna_student', '0002_auto_20180516_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_details',
            new_name='courseDetails',
        ),
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 14, 22, 6, 882000)),
        ),
        migrations.AlterField(
            model_name='enrollcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 14, 22, 6, 911000)),
        ),
    ]
