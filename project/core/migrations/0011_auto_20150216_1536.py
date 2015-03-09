# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150209_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='footer_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='onecolumnmainpage',
            name='footer_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productpage',
            name='footer_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='twocolumnmainpage',
            name='footer_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
    ]
