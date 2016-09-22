#!/usr/bin/python
activate_this = '/var/www/hellobudget.co/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/hellobudget.co/")

from landing import app as application
application.secret_key = '654646498513213168484654654654'
