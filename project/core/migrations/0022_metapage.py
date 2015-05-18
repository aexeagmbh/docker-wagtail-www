# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('core', '0021_auto_20150427_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='wagtailcore.Page', serialize=False, auto_created=True)),
                ('header_title', models.CharField(blank=True, max_length=512)),
                ('header_slogan', models.CharField(blank=True, max_length=512)),
                ('hide_navigation', models.BooleanField(default=False)),
                ('footer_text', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('metapages', wagtail.wagtailcore.fields.StreamField((('whitetwocolumns', wagtail.wagtailcore.blocks.StructBlock((('block1title', wagtail.wagtailcore.blocks.TextBlock()), ('block1subline', wagtail.wagtailcore.blocks.TextBlock())))), ('imagecolumns', wagtail.wagtailcore.blocks.StructBlock((('block3content', wagtail.wagtailcore.blocks.TextBlock()), ('block3thumbnail1', wagtail.wagtailimages.blocks.ImageChooserBlock()))))), null=True, blank=True)),
                ('header_img', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True, to='wagtailimages.Image', related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
