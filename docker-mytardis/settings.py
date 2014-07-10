from os import path
from settings_changeme import *

# Add site specific changes here.

# Turn on django debug mode.
DEBUG = True

# Lots of output...
import logging
SYSTEM_LOG_LEVEL = logging.DEBUG
MODULE_LOG_LEVEL = logging.DEBUG

SYSTEM_LOG_FILENAME = 'request-test.log'
MODULE_LOG_FILENAME = 'tardis-test.log'


# Use the built-in SQLite database for testing.
# The database needs to be named something other than "tardis" to avoid
# a conflict with a directory of the same name.
DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = 'tardis_db'

INSTALLED_APPS = INSTALLED_APPS + ("tardis.apps.atom",)
IS_SECURE = True
REQUIRE_DATAFILE_CHECKSUMS = False

CELERYBEAT_SCHEDULE = dict(CELERYBEAT_SCHEDULE.items() + {
  "update-feeds": {
    "task": "atom_ingest.walk_feeds",
    "schedule": timedelta(seconds=30),
    "args": ('https://ap:4000',)
  },
}.items())

# Post Save Filters
# FIXME Is it ideal to drop dicompng.py into tardis_portal/filters? Might be better off in a separate app?
POST_SAVE_FILTERS = [ ("tardis.tardis_portal.filters.dicompng.make_filter", ["metablob", "http://cai.uq.edu.au/schema/metadata/1"]), ]

# Add Middleware
# FIXME Is this necessary?
MIDDLEWARE_CLASSES = tuple(list(MIDDLEWARE_CLASSES) + ['tardis.tardis_portal.filters.FilterInitMiddleware'])
