from ._base import *

DEBUG = False

ALLOWED_HOSTS = [
    '.thevisualist.org',
    '.visl.ist',
    '.bcw-visualist-master.herokuapp.com',
    '.bcw-visualist-staging.herokuapp.com',
]

INSTALLED_APPS += ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
