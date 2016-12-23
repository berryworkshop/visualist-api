# The visualist
Art, current and archived, from Chicago and beyond.

# Getting running
On a development machine, run either the Django development server:
* `django_project/manage.py runserver`

...or the Heroku local environment, which mimics production:
* `heroku local`

The Heroku server will have niceties like debugging turned off, to show whether things are correctly running for production.

# Start/stop database
* `postgres -D /usr/local/var/postgres`

or for a daemon:

* `pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start` or `stop`


# Running tests

* from https://docs.djangoproject.com/en/1.10/topics/testing/advanced/#integration-with-coverage-py
* `coverage run --source='.' manage.py test`
* `coverage report`
