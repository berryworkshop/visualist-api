from ._base import *

DEBUG = True

ALLOWED_HOSTS = [
    '.localhost',
]

INSTALLED_APPS += ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'visualist',
        'USER': 'visualist',
        'PASSWORD': 'p@ssw0rd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
