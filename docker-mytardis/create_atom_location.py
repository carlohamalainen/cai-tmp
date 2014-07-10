import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

os.system('ln -s bin/django djangosettings.py')

import djangosettings
import sys
sys.path += djangosettings.sys.path

import os.path
sys.path.append(os.path.join(os.getcwd(), 'tardis'))

from django.db import IntegrityError
from tardis.tardis_portal.models.location import Location

try:
    atom = Location(name='atom', url='https://ap:4000', type='external', priority=7, is_available=True, transfer_provider='http')
    atom.save()
    print 'created Location: ' + str(atom)
except IntegrityError:
    print 'Location for atom provider already exists, continuing...'
