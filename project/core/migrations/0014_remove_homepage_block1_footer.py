# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150216_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='block1_footer',
        ),
    ]
