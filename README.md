
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

Install Docker.

Install Python and dependencies.

Set environment variables:

    SECRET_KEY='asdf1234'                   # 50 random chars
    FLASK_CONFIGURATION='development'       # 'development', 'testing', or 'production' (default)
    FLASK_APP='app.py'                      # shouldn't change
    PROJ_PATH="$HOME/Projects/visualist"    # or wherever your root directory is for this

To start local database:

    mkdir -p $PROJ_PATH/neo4j/data/ $PROJ_PATH/neo4j/logs
    docker run -p 7474:7474 -p 7687:7687 \
        -v $PROJ_PATH/neo4j/data:/data -v $PROJ_PATH/neo4j/logs:/logs \
        -e NEO4J_AUTH=none \
        neo4j:3.2

Run application:

    python -m flask run                     # development only; insecure server with auto-reload

Or, to test as in production:

    gunicorn app:app                        # will not auto-reload
