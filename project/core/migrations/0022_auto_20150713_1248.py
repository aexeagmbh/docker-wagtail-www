# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20150427_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='block_signup_button_label',
            new_name='block_conversion_button_label',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='block_signup_title',
            new_name='block_conversion_title',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='activate_olark',
        ),
        migrations.AddField(
            model_name='homepage',
            name='block_conversion_button_url',
            field=models.URLField(blank=True, max_length=128),
            preserve_default=True,
        ),
    ]
