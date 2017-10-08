# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-17 21:47
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0019_auto_20170711_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='toolentry',
            name='field',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='business.ToolField'),
        ),
        migrations.AlterField(
            model_name='toolentry',
            name='tool',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='business.Tool'),
        ),
        migrations.AlterField(
            model_name='toolfield',
            name='icon',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
