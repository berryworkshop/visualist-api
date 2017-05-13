import os
from api import app
from neomodel import config
# from dotenv import load_dotenv

proj_dir = os.path.dirname(
    os.path.abspath(__file__))

config.DATABASE_URL = 'bolt://neo4j:neo4j@localhost:7687' #bolt

# secret vars
# dotenv_path = os.path.join(proj_dir, '.env')
# load_dotenv(dotenv_path)

if __name__ == '__main__':
    app.run(debug=True)
