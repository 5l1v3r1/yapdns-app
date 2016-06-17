# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 09:49
from __future__ import unicode_literals

import core.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('secret_key', models.CharField(default=core.models.generate_secret_key, editable=False, max_length=48)),
            ],
        ),
    ]
