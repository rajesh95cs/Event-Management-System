# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_id', models.CharField(max_length=20)),
                ('Empfirst_name', models.CharField(max_length=100)),
                ('Emplast_name', models.CharField(max_length=100)),
                ('Emp_des', models.CharField(max_length=100)),
                ('hired_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
