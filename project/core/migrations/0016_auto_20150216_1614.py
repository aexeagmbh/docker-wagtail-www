# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('core', '0015_auto_20150216_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='header_img',
            field=models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='onecolumnmainpage',
            name='header_img',
            field=models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productpage',
            name='header_img',
            field=models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, related_name='+'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='twocolumnmainpage',
            name='header_img',
            field=models.ForeignKey(to='wagtailimages.Image', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, related_name='+'),
            preserve_default=True,
        ),
    ]
