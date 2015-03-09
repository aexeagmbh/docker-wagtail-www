# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0006_auto_20150203_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwoColumnMainPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, to='wagtailcore.Page', serialize=False, auto_created=True, primary_key=True)),
                ('subtitle', wagtail.wagtailcore.fields.RichTextField()),
                ('teaser', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('main_content_left', wagtail.wagtailcore.fields.RichTextField()),
                ('main_content_right', wagtail.wagtailcore.fields.RichTextField()),
                ('conversion_title', models.CharField(blank=True, max_length=256)),
                ('conversion_url', models.URLField(blank=True)),
                ('conversion_button_label', models.CharField(blank=True, max_length=256)),
                ('foot_row', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
