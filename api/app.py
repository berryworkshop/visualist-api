import pymongo
import os
from eve import Eve

db_user   = os.getenv('MONGO_USERNAME', 'visualist_admin')
db_pass   = os.getenv('MONGO_PASSWORD')
db_server = os.getenv('MONGO_SERVER', 'localhost')
db_port   = os.getenv('MONGO_PORT', 27017)
db_name   = os.getenv('MONGO_DBNAME', 'visualist')

global_settings = {
    'DOMAIN': {'people': {}},
    'XML': False,
    'MONGO_URI': f'mongodb://{db_user}:{db_pass}@{db_server}:{db_port}/{db_name}',
}

app = Eve(settings=global_settings)

if __name__ == '__main__':
    app.run()
