#!/usr/bin/env python3

from sys.path import insert
from logging import basicConfig
from site import app

basicConfig(stream=sys.stderr)
insert(0, '/var/www/ds-form-site/')

app.secret_key = 'this is a very super secret key'

