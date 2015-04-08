# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_teampage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampage',
            name='emploees',
            field=wagtail.wagtailcore.fields.StreamField((('emploee', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('jobTitle', wagtail.wagtailcore.blocks.CharBlock(label='Job title')), ('tel', wagtail.wagtailcore.blocks.CharBlock(label='Telephone')), ('email', wagtail.wagtailcore.blocks.CharBlock(label='Email')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())))),)),
            preserve_default=True,
        ),
    ]
