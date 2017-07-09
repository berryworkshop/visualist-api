import os
import pymongo
from eve import Eve
from .settings import development, production

if (os.getenv('SETTINGS_MODE') == 'development'):
    app = Eve(settings=development.settings)
else:
    app = Eve(settings=production.settings)


if __name__ == '__main__':
    app.run()
