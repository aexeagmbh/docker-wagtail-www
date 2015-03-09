# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0008_auto_20150203_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, to='wagtailcore.Page', parent_link=True)),
                ('header_title', models.CharField(max_length=512, blank=True)),
                ('header_slogan', models.CharField(max_length=512, blank=True)),
                ('block1_content', wagtail.wagtailcore.fields.RichTextField()),
                ('block2_content', wagtail.wagtailcore.fields.RichTextField()),
                ('block3_content', wagtail.wagtailcore.fields.RichTextField()),
                ('block4_content', wagtail.wagtailcore.fields.RichTextField()),
                ('conversion_title', models.CharField(max_length=256, blank=True)),
                ('conversion_url', models.URLField(blank=True)),
                ('conversion_button_label', models.CharField(max_length=256, blank=True)),
                ('foot_row', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('block1_thumbnail', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', null=True, related_name='+')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
