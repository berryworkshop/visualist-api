
888    888                             d8b                            888 d8b          888    
888    888                             Y8P                            888 Y8P          888    
888    888                                                            888              888    
888888 88888b.   .d88b.       888  888 888 .d8888b  888  888  8888b.  888 888 .d8888b  888888 
888    888 "88b d8P  Y8b      888  888 888 88K      888  888     "88b 888 888 88K      888    
888    888  888 88888888      Y88  88P 888 "Y8888b. 888  888 .d888888 888 888 "Y8888b. 888    
Y88b.  888  888 Y8b.           Y8bd8P  888      X88 Y88b 888 888  888 888 888      X88 Y88b.  
 "Y888 888  888  "Y8888         Y88P   888  88888P'  "Y88888 "Y888888 888 888  88888P'  "Y888


Art, current and archived, from Chicago and beyond.

---

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
