#!/bin/bash

set -e

python3 manage.py runscript create_admin
python3 manage.py compress
