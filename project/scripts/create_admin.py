#!/usr/bin/env python
import logging
from django.contrib.auth.models import User


def run(*args):
    if len(User.objects.filter(username='admin')) == 0:
        logging.info('Creating superuser admin:admin')
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
