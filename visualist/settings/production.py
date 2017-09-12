from ._base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [
    '.thevisualist.org',
    '.visl.ist',
    '.bcw-visualist-master.herokuapp.com',
    '.bcw-visualist-staging.herokuapp.com',
]

INSTALLED_APPS += ()

## database connections handled by Heroku, via DATABASE_URL env var
DATABASES['default'] =  dj_database_url.config()
