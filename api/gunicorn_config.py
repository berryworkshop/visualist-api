import os

if os.environ.get('SETTINGS_MODE') == 'development':
    reload = True
    loglevel = 'debug'
    accesslog = '-'
elif os.environ.get('SETTINGS_MODE') == 'test':
    pass
else:
    pass
