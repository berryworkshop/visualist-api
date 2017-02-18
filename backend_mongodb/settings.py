from schemas.schema import (
    nodes_schema,
    edges_schema,
    collections_schema,
    users_schema,
    files_schema,
    locations_schema,
    tags_schema,
    pages_schema,
)

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

nodes = {
    'additional_lookup': {
        'url': 'regex("[-\w]+")',
        'field': 'slug'
    },
    'schema': nodes_schema
}
edges = {
    'schema': edges_schema
}
collections = {
    'schema': collections_schema
}
users = {
    'schema': users_schema
}
files = {
    'schema': files_schema
}
locations = {
    'schema': locations_schema
}
tags = {
    'schema': tags_schema
}
pages = {
    'schema': pages_schema
}

DOMAIN = {
    'nodes': nodes,
    'edges': edges,
    'collections': collections,
    'users': users,
    'files': files,
    'locations': locations,
    'tags': tags,
    'pages': pages,
}
