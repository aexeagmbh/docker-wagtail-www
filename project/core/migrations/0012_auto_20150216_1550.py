# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150216_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='block1_subline',
            field=models.CharField(blank=True, max_length=1024),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block5_content',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block5_title',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
    ]
