import os
import yaml
import pkg_resources
from .schema import (
    CollectionSchema,
    EventSchema,
    OrganizationSchema,
    PageSchema,
    PersonSchema,
    PlaceSchema,
    UserSchema,
    WorkSchema,
)

db_user   = os.getenv('MONGO_USERNAME', 'visualist_admin')
db_pass   = os.getenv('MONGO_PASSWORD')
db_server = os.getenv('MONGO_SERVER', 'localhost')
db_port   = os.getenv('MONGO_PORT', 27017)
db_name   = os.getenv('MONGO_DBNAME', 'visualist')


collections = {
    'resource_methods': ['GET', 'POST'],
    'schema': CollectionSchema,
}
events = {
    'resource_methods': ['GET', 'POST'],
    'schema': EventSchema,
}
organizations = {
    'resource_methods': ['GET', 'POST'],
    'schema': OrganizationSchema,
}
pages = {
    'resource_methods': ['GET', 'POST'],
    'schema': PageSchema,
}
people = {
    'item_title': 'person',
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'schema': PersonSchema,
}
places = {
    'resource_methods': ['GET', 'POST'],
    'schema': PlaceSchema,
}
tags = {
    'resource_methods': ['GET', 'POST'],
    'schema': OrganizationSchema,
}
users = {
    'resource_methods': ['GET', 'POST'],
    'schema': UserSchema,
}
works = {
    'resource_methods': ['GET', 'POST'],
    'schema': WorkSchema,
}


settings = {
    'DOMAIN': {
        'people': people,
        'collections': collections,
        'events': events,
        'organizations': organizations,
        'pages': pages,
        'places': places,
        'tags': tags,
        'users': users,
        'works': works,
    },
    'URL_PREFIX': 'api',
    'API_VERSION': 'v1',
    'DATE_FORMAT': '%Y-%m-%dT%H:%M:%S',
    'XML': False,
    'MONGO_URI': f'mongodb://{db_user}:{db_pass}@{db_server}:{db_port}/{db_name}',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
}
