# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_create_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Homepage'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_content1',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_content2',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_content3',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_content4',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_footer',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_subtitle',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block1_title',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
    ]
