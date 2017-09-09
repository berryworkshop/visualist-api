import os

env = os.environ.get('NODE_ENV', 'production')

if env == 'development':
    from .development import *
elif env == 'testing':
    from .testing import *
else: # env == 'production'
    from .production import *
