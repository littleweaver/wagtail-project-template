from __future__ import absolute_import, unicode_literals

import os
import subprocess
from django.conf import settings
from .base import *  # noqa: F403, F401

# SECURITY WARNING: keep the secret key used in production secret!
# This MUST BE CHANGED for every project
SECRET_KEY = '-hf!6+rx$-55pyf6tekfkers#7cfn-_d#4f6*vnr-+vz82lqz_'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *  # noqa: F403, F401
except ImportError:
    pass

if settings.DEBUG:
    # Fix for https://github.com/jazzband/django-debug-toolbar/issues/950
    DEBUG_TOOLBAR_CONFIG = {
        'SKIP_TEMPLATE_PREFIXES': (
            'django/forms/widgets/',
            'admin/widgets/',
        ),
        'DISABLE_PANELS': {
            'debug_toolbar.panels.redirects.RedirectsPanel',
            'debug_toolbar.panels.redirects.TemplatesPanel'
        },
    }

    INSTALLED_APPS.append('debug_toolbar')  # noqa: F405
    # Needs to be injected relatively early in the MIDDLEWARE list
    MIDDLEWARE.insert(4, 'debug_toolbar.middleware.DebugToolbarMiddleware')  # noqa: F405
    INTERNAL_IPS = []

DATABASES = {
    'default': dj_database_url.config(default="sqlite:///db.sqlite3")
}
