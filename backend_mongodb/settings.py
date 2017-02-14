
# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'visualist'
XML = False
API_VERSION = 'v1'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

records_schema = {
    "type": {
        'type': 'list',
        'required': True,
        'allowed': [
            'person',
            'organization',
            'work',
            'venue',
            'event',
            'thing',
            'ephemeron',
            'page',
        ]
    },
    "slug": {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
        'unique': True,
    },
    "name": {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
    },
    "caption": {
        'type': 'string',
        'minlength': 1,
        'maxlength': 250,
    },
    "is_featured": {
        'type': 'boolean',
        'default': False,
    },
    "language": {
        'type': 'string',
        # 'required': True,
        'default': 'en-us',
        'allowed': [
            'en-us',
        ]
    },
}

records = {
    'additional_lookup': {
        'url': 'regex("[-\w]+")',
        'field': 'slug'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': records_schema,
}

DOMAIN = {
    'records': records,
}
