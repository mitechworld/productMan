# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-10 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180210_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='zone',
            new_name='district',
        ),
    ]
