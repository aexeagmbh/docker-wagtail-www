# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_twocolumnmainpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='header_slogan',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='header_title',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='onecolumnmainpage',
            name='header_slogan',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='onecolumnmainpage',
            name='header_title',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='twocolumnmainpage',
            name='header_slogan',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='twocolumnmainpage',
            name='header_title',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
    ]
