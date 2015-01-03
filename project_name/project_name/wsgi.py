import os
from os.path import abspath, dirname
from sys import path

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)
os.environ["DJANGO_SETTINGS_MODULE"] = "{{ project_name }}.settings.prod"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
