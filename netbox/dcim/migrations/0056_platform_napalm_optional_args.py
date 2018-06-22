# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0055_virtualchassis_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='napalm_optional_args',
            field=models.CharField(blank=True, help_text='Comma separated key=value pairs passed via optional_args to the driver.', max_length=200, verbose_name='NAPALM optional arguments'),
        ),
    ]
