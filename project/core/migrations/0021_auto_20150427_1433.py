# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20150422_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='activate_olark',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='onecolumnmainpage',
            name='activate_olark',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productpage',
            name='activate_olark',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='twocolumnmainpage',
            name='activate_olark',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
