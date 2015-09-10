# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('core', '0022_auto_20150713_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversalStreamPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, to='wagtailcore.Page', serialize=False, auto_created=True, primary_key=True)),
                ('header_title', models.CharField(blank=True, max_length=512)),
                ('header_slogan', models.CharField(blank=True, max_length=512)),
                ('hide_navigation', models.BooleanField(default=False)),
                ('footer_text', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('content', wagtail.wagtailcore.fields.StreamField((('teaser_area', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=True))), template='core/blocks/teaster_area.html')),))),
                ('header_img', models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
