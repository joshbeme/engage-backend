# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-03 09:55
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0002_auto_20180214_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendaitem',
            name='new_body',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), default=[], size=None),
        ),
    ]
