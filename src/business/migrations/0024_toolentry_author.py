# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-28 09:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0023_auto_20170731_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolentry',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]