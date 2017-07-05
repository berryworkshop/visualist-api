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
    # 'MONGO_URI': f'mongodb://{db_user}:{db_pass}@visualist-shard-00-00-aairr.mongodb.net:{db_port},visualist-shard-00-01-aairr.mongodb.net:{db_port},visualist-shard-00-02-aairr.mongodb.net:{db_port}/{db_name}?ssl=true&replicaSet=visualist-shard-0&authSource=admin',
}

app = Eve(settings=global_settings)

if __name__ == '__main__':
    app.run()

