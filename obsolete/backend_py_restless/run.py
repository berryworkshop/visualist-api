import os
from api import app
# from dotenv import load_dotenv

proj_dir = os.path.dirname(
    os.path.abspath(__file__))

# secret vars
# dotenv_path = os.path.join(proj_dir, '.env')
# load_dotenv(dotenv_path)

if __name__ == '__main__':
    app.run(debug=True)
