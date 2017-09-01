#!/usr/bin/env python3

from sys.path import insert
from logging import basicConfig
from ds-form-site import app

basicConfig(stream=sys.stderr)
insert(0, '/var/www/ds-demo/')

