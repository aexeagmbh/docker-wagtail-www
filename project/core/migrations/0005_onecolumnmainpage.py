# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0004_auto_20150202_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneColumnMainPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='wagtailcore.Page', serialize=False, primary_key=True)),
                ('subtitle', wagtail.wagtailcore.fields.RichTextField()),
                ('row1_teaser1', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('row1_teaser2', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('row1_teaser3', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('main_content', wagtail.wagtailcore.fields.RichTextField()),
                ('conversion_banner', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('foot_row', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
