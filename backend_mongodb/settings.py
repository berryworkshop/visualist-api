import .schema

# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'visualist'
API_VERSION = 'v1'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
AUTO_CREATE_LISTS:
    True

records = {
    'additional_lookup': {
        'url': 'regex("[-\w]+")',
        'field': 'slug'
    },
    'schema': schema.records,
}
people = {
    **records,
    **{
        'schema': schema.people,
    }
}
locations = {
    **records,
    **{
        'schema': schema.locations,
    }
}
works = {
    **records,
    **{
        'schema': schema.works,
    }
}

DOMAIN = {
    'people': people,
    'locations': locations,
    'works': works,
}
