import os

if os.environ.get('SETTINGS_MODE') == 'development':
    reload = True
    loglevel = 'debug'
    accesslog = '-'
elif os.environ.get('SETTINGS_MODE') == 'test':
    pass
else: # 'production'
    pass

bind = '0.0.0.0:8000'
