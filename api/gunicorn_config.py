import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if os.environ.get('SETTINGS_MODE') == 'development':
    reload = True
    loglevel = 'debug'
    accesslog = '-'
    access_log_format = \
        '%(h)s %(l)s %(u)s %(t)s "%(r)s" status: %(s)s, %(b)s bytes "%(f)s"'
elif os.environ.get('SETTINGS_MODE') == 'test':
    pass
else:
    pass
