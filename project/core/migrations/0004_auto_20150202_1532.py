# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('core', '0003_auto_20150202_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='block2_content1',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block2_content2',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block2_content3',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block2_content4',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block2_title',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block3_content1',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block3_content2',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block3_content3',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block3_content4',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block3_thumbnail1',
            field=models.ForeignKey(null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block3_thumbnail2',
            field=models.ForeignKey(null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block3_thumbnail3',
            field=models.ForeignKey(null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block3_thumbnail4',
            field=models.ForeignKey(null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block4_content1',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block4_content2',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block_signup_button_label',
            field=models.CharField(blank=True, max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='block_signup_title',
            field=models.CharField(blank=True, max_length=512),
            preserve_default=True,
        ),
    ]
