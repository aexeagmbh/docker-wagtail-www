# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ax1510HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
            ],
            options={
                'description': 'The top level homepage for AX. Static version from October 15.',
                'verbose_name': 'AX 1510 Static Homepage',
            },
            bases=('wagtailcore.page',),
        ),
    ]
