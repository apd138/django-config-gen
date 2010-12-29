import __main__
import os
from django.contrib.sites.models import Site

PROJECT_ROOT = os.path.abspath(os.path.dirname(__main__.__file__))
LOG_DIR = os.path.join(PROJECT_ROOT ,'logs')

_config_dir = os.path.join(PROJECT_ROOT ,'config')
TEMPLATES_DIR = os.path.join(_config_dir ,'templates')
GENERATED_DIR = os.path.join(_config_dir ,'generated')

#Error is thrown when running "./manage.py syncdb" for the first time and this app is installed.

def _get_host():
	return Site.objects.get_current().domain.split(':')[0]

HOST = property(_get_host)