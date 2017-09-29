import os
import sys

# which environment?
if 'test' in sys.argv:
    from .testing import *
elif (os.environ.get('MODE', 'production') == 'development'):
    from .development import *
else:
    from .production import *
