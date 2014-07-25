from os import path
from settings_changeme import *

# Add site specific changes here.

# Turn on django debug mode.
DEBUG = True

# Lots of output...
import logging
SYSTEM_LOG_LEVEL = logging.DEBUG
MODULE_LOG_LEVEL = logging.DEBUG

SYSTEM_LOG_FILENAME = '/var/log/request-test.log'
MODULE_LOG_FILENAME = '/var/log/tardis-test.log'

DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
DATABASES['default']['NAME'] = 'tardis'
DATABASES['default']['USER'] = 'admin'
DATABASES['default']['PASSWORD'] = 'admin'
DATABASES['default']['HOST'] = '127.0.0.1'
DATABASES['default']['PORT'] = ''

# When using the Atom provider:
#
# INSTALLED_APPS = INSTALLED_APPS + ("tardis.apps.atom",)
# IS_SECURE = True
# REQUIRE_DATAFILE_CHECKSUMS = False
#
# CELERYBEAT_SCHEDULE = dict(CELERYBEAT_SCHEDULE.items() + {
#   "update-feeds": {
#     "task": "atom_ingest.walk_feeds",
#     "schedule": timedelta(seconds=30),
#     "args": ('https://cai-murdoch.cai.uq.edu.au:4001',)
#   },
# }.items())

# Post Save Filters
# POST_SAVE_FILTERS = [ ("tardis.tardis_portal.filters.dicom.dicompng.make_filter", ["metablob", "http://cai.uq.edu.au/schema/metadata/1"]), ]

# Middleware
# MIDDLEWARE_CLASSES = tuple(list(MIDDLEWARE_CLASSES) + ['tardis.tardis_portal.filters.FilterInitMiddleware'])
# FILTER_MIDDLEWARE = (("tardis.tardis_portal.filters", "FilterInitMiddleware"),)

FILE_STORE_PATH = '/mytardis_store'
STAGING_PATH    = '/mytardis_staging'

# Django places a temporary uploaded file here and then does a save_move
# to the final name in FILE_STORE_PATH. So ideally the directories
# FILE_UPLOAD_TEMP_DIR and FILE_STORE_PATH will be on the same file system.
FILE_UPLOAD_TEMP_DIR = '/other'
