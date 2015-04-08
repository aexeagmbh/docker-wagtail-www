# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('core', '0016_auto_20150216_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='wagtailcore.Page', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('name', models.CharField(max_length=50)),
                ('jobTitle', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('emploees', wagtail.wagtailcore.fields.StreamField((('emploee', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('jobTitle', wagtail.wagtailcore.blocks.CharBlock(label='Name')), ('email', wagtail.wagtailcore.blocks.CharBlock(label='Email')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())))),))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
