# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-16 12:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yagna_student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 5, 16, 12, 42, 48, 182000))),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 12, 42, 48, 153000)),
        ),
        migrations.AddField(
            model_name='enrollcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yagna_student.Course'),
        ),
        migrations.AddField(
            model_name='enrollcourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
