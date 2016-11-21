from .base import *

# secret vars
SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

DEBUG = False

ADMINS = [
    ('Allan', 'allan.berry@gmail.com'),
    ]

ALLOWED_HOSTS = [
    '.berryworkshop.com',
    '.allanberry.com',
    'localhost',
    'bcw-visualist.herokuapp.com',
    'bcw-visualist-staging.herokuapp.com',
    ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'artcase_db',
        'USER': 'artcase_admin',
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
#     }
# }

# should be moved to amazon?
STATIC_ROOT = '%s/static/' % BASE_DIR

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'