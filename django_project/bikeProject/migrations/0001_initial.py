# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentCount', models.IntegerField()),
            ],
        ),
    ]
