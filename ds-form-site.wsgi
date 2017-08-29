#!/usr/bin/env python3

from sys.path import insert
from logging import basicConfig
from ds-form-site import app

basicConfig(stream=sys.stderr)
insert(0, '/var/www/ds-form-site/')

app.secret_key = 'kOthrC4RFjVQLgTG7JfqfUl1di7dXSTD3buW7GVdWuXw9+wmsLw1v+o/lNd60Ranjt4LXYOIaC01DU7sqflMng=='

