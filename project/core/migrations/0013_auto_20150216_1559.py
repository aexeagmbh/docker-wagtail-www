# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150216_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='block1_conversion_button_label',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_conversion_title',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_conversion_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
