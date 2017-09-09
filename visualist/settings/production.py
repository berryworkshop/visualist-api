from ._base import *

DEBUG = False

ALLOWED_HOSTS = [
    'thevisualist.org',
    'visl.ist',
]

INSTALLED_APPS += ()

MIDDLEWARE_CLASSES += (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

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
