import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
INTERNAL_IPS = '127.0.0.1'
ALLOWED_HOSTS = ['127.0.0.1','localhost', 'backend']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'DB': 'dev',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

DB_HOST = os.getenv('DB_HOST', 'localhost')
DATABASES['default']['HOST'] = DB_HOST
