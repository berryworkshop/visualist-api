from . import _base
import os

settings = {**_base.settings,
    'X_DOMAINS': '*',
    'DEBUG': True,
}
