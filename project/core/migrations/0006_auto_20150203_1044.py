# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_onecolumnmainpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onecolumnmainpage',
            name='conversion_banner',
        ),
        migrations.AddField(
            model_name='onecolumnmainpage',
            name='conversion_button_label',
            field=models.CharField(blank=True, max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='onecolumnmainpage',
            name='conversion_title',
            field=models.CharField(blank=True, max_length=256),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='onecolumnmainpage',
            name='conversion_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
