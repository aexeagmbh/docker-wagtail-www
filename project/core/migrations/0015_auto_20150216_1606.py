# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_homepage_block1_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='block1_button1_label',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_button1_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_button2_label',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_button2_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_button3_label',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_button3_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_button4_label',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_button4_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
