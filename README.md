
888    888                             d8b                            888 d8b          888
888    888                             Y8P                            888 Y8P          888
888    888                                                            888              888
888888 88888b.   .d88b.       888  888 888 .d8888b  888  888  8888b.  888 888 .d8888b  888888
888    888 "88b d8P  Y8b      888  888 888 88K      888  888     "88b 888 888 88K      888
888    888  888 88888888      Y88  88P 888 "Y8888b. 888  888 .d888888 888 888 "Y8888b. 888
Y88b.  888  888 Y8b.           Y8bd8P  888      X88 Y88b 888 888  888 888 888      X88 Y88b.
 "Y888 888  888  "Y8888         Y88P   888  88888P'  "Y88888 "Y888888 888 888  88888P'  "Y888


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

# Getting running
On a development machine, run either the Django development server:
* `django_project/manage.py runserver`

...or the Heroku local environment, which mimics production:
* `heroku local`

The Heroku server will have niceties like debugging turned off, to show whether things are correctly running for production.


# Start/stop database
* `neo4j start`


# Start backend API
* `python backend/run.py`


# Running tests

* python -m unittest backend.api.tests
