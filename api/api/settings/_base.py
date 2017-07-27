import os
import yaml
import pkg_resources

db_user   = os.getenv('MONGO_USERNAME', 'visualist_admin')
db_pass   = os.getenv('MONGO_PASSWORD')
db_server = os.getenv('MONGO_SERVER', 'localhost')
db_port   = os.getenv('MONGO_PORT', 27017)
db_name   = os.getenv('MONGO_DBNAME', 'visualist')

s = pkg_resources.resource_string(__name__, '/schema.yaml')
schema = yaml.load(s)



collections = {
    'resource_methods': ['GET', 'POST'],
    'schema': schema['CollectionSchema'],
}
events = {
    'resource_methods': ['GET', 'POST'],
    'schema': schema['EventSchema'],
}
organizations = {
    'resource_methods': ['GET', 'POST'],
    'schema': schema['OrganizationSchema'],
}
pages = {
    'resource_methods': ['GET', 'POST'],
    'schema': schema['PageSchema'],
}
people = {
    'item_title': 'person',
    'resource_methods': ['GET', 'POST'],
    'schema': schema['PersonSchema'],
}
places = {
    'resource_methods': ['GET', 'POST'],
    'schema': schema['PlaceSchema'],
}
roles = {
    'resource_methods': ['GET', 'POST'],
    'schema': schema['RoleSchema'],
}
tags = {
    'resource_methods': ['GET', 'POST'],
    'schema': schema['OrganizationSchema'],
}
users = {
    'resource_methods': ['GET', 'POST'],
    'schema': schema['UserSchema'],
}
works = {
    'resource_methods': ['GET', 'POST'],
    'schema': schema['WorkSchema'],
}


settings = {
    'DOMAIN': {
        'people': people,
        'collections': collections,
        'events': events,
        'organizations': organizations,
        'pages': pages,
        'places': places,
        'roles': roles,
        'tags': tags,
        'users': users,
        'works': works,
    },
    'XML': False,
    'MONGO_URI': f'mongodb://{db_user}:{db_pass}@{db_server}:{db_port}/{db_name}',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
}
