# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-12 12:25
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170712_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
