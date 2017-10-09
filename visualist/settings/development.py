from ._base import *

DEBUG = True

ALLOWED_HOSTS = [
    '.localhost',
]

INSTALLED_APPS += ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vis_db',
        'USER': 'vis_user',
        'PASSWORD': 'vis_pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
