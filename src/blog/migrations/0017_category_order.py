# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-20 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20170720_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]