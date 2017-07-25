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

people = {
    'item_title': 'person',
    'resource_methods': ['GET', 'POST'],
    'schema': schema['PersonSchema'],
}

settings = {
    'DOMAIN': {'people': people},
    'XML': False,
    'MONGO_URI': f'mongodb://{db_user}:{db_pass}@{db_server}:{db_port}/{db_name}',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'PUT', 'DELETE'],
}
