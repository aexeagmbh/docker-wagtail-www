# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150409_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampage',
            name='employees',
            field=wagtail.wagtailcore.fields.StreamField((('employee', wagtail.wagtailcore.blocks.StructBlock((('forename', wagtail.wagtailcore.blocks.CharBlock()), ('surname', wagtail.wagtailcore.blocks.CharBlock()), ('job_title', wagtail.wagtailcore.blocks.CharBlock()), ('telephone', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('email', wagtail.wagtailcore.blocks.CharBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())))),), null=True, blank=True),
            preserve_default=True,
        ),
    ]
