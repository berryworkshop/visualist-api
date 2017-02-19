from schemas import (
    nodes, edges, collections, users, files, locations, tags, pages)

# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'visualist'
API_VERSION = 'v1'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
AUTO_CREATE_LISTS = True

# development only
XML = False
IF_MATCH = False

DOMAIN = {
    'nodes': {
        'additional_lookup': {
            'url': 'regex("[-\w]+")',
            'field': 'slug'
        },
        'schema': {**nodes.schema}
    },
    'edges': {
        'schema': {**edges.schema}
    },
    'collections': {
        'schema': {**collections.schema}
    },
    'users': {
        'schema': {**users.schema}
    },
    'files': {
        'schema': {**files.schema}
    },
    'locations': {
        'schema': {**locations.schema}
    },
    'tags': {
        'schema': {**tags.schema}
    },
    'pages': {
        'schema': {**pages.schema}
    },
}
