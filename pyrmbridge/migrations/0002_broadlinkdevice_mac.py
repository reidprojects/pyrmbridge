# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-07 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyrmbridge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='broadlinkdevice',
            name='mac',
            field=models.CharField(default='34:ea:34:c7:8f:c8', max_length=30),
            preserve_default=False,
        ),
    ]
