    888    888
    888    888
    888    888
    888888 88888b.   .d88b.
    888    888 "88b d8P  Y8b
    888    888  888 88888888
    Y88b.  888  888 Y8b.
     "Y888 888  888  "Y8888

             d8b                            888 d8b          888
             Y8P                            888 Y8P          888
                                            888              888
    888  888 888 .d8888b  888  888  8888b.  888 888 .d8888b  888888
    888  888 888 88K      888  888     "88b 888 888 88K      888
    Y88  88P 888 "Y8888b. 888  888 .d888888 888 888 "Y8888b. 888
     Y8bd8P  888      X88 Y88b 888 888  888 888 888      X88 Y88b.
      Y88P   888  88888P'  "Y88888 "Y888888 888 888  88888P'  "Y888

The visualist: people and their art.
Copyright (C) 2016  Allan J. Berry

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

For more information, contact Allan Berry at allan.berry@gmail.com.  Thanks.

---

The Visualist
===

It's alive!


Database
---

Currently, I'm running MongoDB as the database, which seems OK.  (Maybe in the future this will change.)  But for now, for development, you'll need a local `Mongod` process running, with a database `visualist`, and an admin user `visualist_admin`.  See the environment variables below for more details.


Environment Variables
---

This project needs these environment variables to be set, probably via a `.env` file (check out `autoenv` on Mac... works great):

At the `/visualist` level, something like:

    SECRET_KEY=<<50 char random key>>
    PROJ_PATH=$HOME/Projects/visualist

At the `/api` level:

    SETTINGS_MODE=development
    FLASK_APP=api
    FLASK_DEBUG=true
    MONGO_USERNAME=visualist_admin
    MONGO_PASSWORD=<<db_password>>
    MONGO_SERVER=localhost
    MONGO_PORT=27017
    MONGO_DBNAME=visualist


Deploy
---

General deployment for the API and NGINX happens via Git and Docker.

    git push origin master
    ssh visualist_digitalocean
    cd /srv/visualist
    git pull origin master
    docker-compose stop
    docker-compose up --build -d
    exit

Environment variables for the Digital Ocean VM are located at `/etc/environment`.

Deployment for the Frontend is detailed in that directory's README.

Running the API's development server (and an alternative deployment for the API to Heroku) is detailed in that directory's README.


Credits
---

a lot of the Docker setup was detailed here (thanks):

  * http://www.patricksoftwareblog.com/how-to-use-docker-and-docker-compose-to-create-a-flask-application/
  * http://matthewminer.com/2015/01/25/docker-dev-environment-for-web-app.html
  * http://www.patricksoftwareblog.com/how-to-configure-nginx-for-a-flask-web-application/
