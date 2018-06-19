import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
INTERNAL_IPS = '127.0.0.1'
ALLOWED_HOSTS = ['127.0.0.1','localhost', 'backend']


import django_heroku
django_heroku.settings(locals())