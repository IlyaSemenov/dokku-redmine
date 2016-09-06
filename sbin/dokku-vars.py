#!/usr/bin/env python3

import json
import os
from urllib.parse import urlparse


def print_var(var, value):
	print('export {}={}'.format(var, json.dumps(value)))

db_url = os.getenv('DATABASE_URL')
if not db_url:
	raise Exception("DATABASE_URL not set. Did you run dokku postgres:link?")
db_urlp = urlparse(db_url)
db_adapter_map = {'postgres': 'postgresql', 'mysql': 'mysql2'}
db_adapter = db_adapter_map.get(db_urlp.scheme)
if not db_adapter:
	raise Exception("Unsupported database: {} (supported: {})".format(db_urlp.scheme, ", ".join(sorted(db_adapter_map.keys()))))
print_var("DB_ADAPTER", db_adapter)
print_var("DB_HOST", db_urlp.hostname)
print_var("DB_PORT", str(db_urlp.port or 5432))
print_var("DB_USER", db_urlp.username)
print_var("DB_PASS", db_urlp.password)
print_var("DB_NAME", db_urlp.path[1:])
