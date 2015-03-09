# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_productpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onecolumnmainpage',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='twocolumnmainpage',
            name='subtitle',
        ),
    ]
