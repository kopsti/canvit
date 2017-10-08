# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 22:03
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20170719_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
