# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_sku_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='started_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
