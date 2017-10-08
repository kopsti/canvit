# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-07 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_tool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmc',
            name='author',
        ),
        migrations.RemoveField(
            model_name='bmc',
            name='company',
        ),
        migrations.RemoveField(
            model_name='bmcentry',
            name='bmc',
        ),
        migrations.RemoveField(
            model_name='bmcentry',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vpc',
            name='author',
        ),
        migrations.RemoveField(
            model_name='vpc',
            name='company',
        ),
        migrations.RemoveField(
            model_name='vpcentry',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vpcentry',
            name='vpc',
        ),
        migrations.RemoveField(
            model_name='swot',
            name='status',
        ),
        migrations.DeleteModel(
            name='BMC',
        ),
        migrations.DeleteModel(
            name='BMCEntry',
        ),
        migrations.DeleteModel(
            name='BMCField',
        ),
        migrations.DeleteModel(
            name='VPC',
        ),
        migrations.DeleteModel(
            name='VPCEntry',
        ),
        migrations.DeleteModel(
            name='VPCField',
        ),
    ]
