API
===

A subproject of the larger Visualist, the API requires hosting on its own.

boot
---

I originally devloped this application to be hosted on Heroku, then converted it for Docker, then went back to Heroku.  Now I'm leaning toward Docker again.  So it's currently a combination of both.

Locally, you can run in at least four ways (I know, right?):

1. using Docker, from the root (`api/..`) directory (runs Gunicorn in a container, through an Nginx proxy):

    export MONGO_SERVER=docker.for.mac.localhost
    docker-compose up --build

2. from the `api` directory, using Gunicorn directly (don't forget to reload the environment variables in `api/.env`):

    gunicorn -c gunicorn_config.py api:app

3. from the `api` directory, using the Heroku CLI (also uses Gunicorn behind the scenes):

    heroku local

4. or, using the Flask server, from the `api` directory:

    flask run


deploy to Heroku
---

Deployment instructions to Digital Ocean are in the parent README.

1. From the root directory (`api/..`):

    git subtree push --prefix=api api staging

2. ...or:

    git subtree push --prefix=api api master
