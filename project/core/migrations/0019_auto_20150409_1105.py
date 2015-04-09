# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('core', '0018_auto_20150408_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teampage',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='emploees',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='jobTitle',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teampage',
            name='tel',
        ),
        migrations.AddField(
            model_name='teampage',
            name='employees',
            field=wagtail.wagtailcore.fields.StreamField((('employee', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock()), ('job_title', wagtail.wagtailcore.blocks.CharBlock()), ('telephone', wagtail.wagtailcore.blocks.CharBlock()), ('email', wagtail.wagtailcore.blocks.CharBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())))),), blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teampage',
            name='footer_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teampage',
            name='header_img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teampage',
            name='header_slogan',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teampage',
            name='header_title',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
    ]
