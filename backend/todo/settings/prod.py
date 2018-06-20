import os

import dj_database_url

from .base import *

DEBUG = True
INTERNAL_IPS = '127.0.0.1'
ALLOWED_HOSTS = ['127.0.0.1','localhost', 'backend', 'shedafullstackdemo.herokuapp.com']

DATABASE_URI = os.environ['DATABASE_URL']
DATABASES['default'] = dj_database_url.config(default=DATABASE_URI)

WEBPACK_LOADER = {
    'DEFAULT': {
            'BUNDLE_DIR_NAME': 'bundles/',
            'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.prod.json'),
        }
}
