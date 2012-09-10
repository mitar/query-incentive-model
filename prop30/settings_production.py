from settings import *

# Secrets are in a separate file so they are not visible in public repository
from secrets import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Sets the URL root for the site, this makes sure all the paths/stylesheets/scripts work
URL_ROOT = 'http://opinion.berkeley.edu/ca-prop-30-awareness/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# SECRET_KEY is in secrets

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
