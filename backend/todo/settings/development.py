import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
INTERNAL_IPS = '127.0.0.1'
ALLOWED_HOSTS = ['127.0.0.1','localhost', 'backend']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
