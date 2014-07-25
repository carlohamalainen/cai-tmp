import sys

sys.path.append('/opt/mytardis')
from append_django_paths import *

from django.db import IntegrityError
from tardis.tardis_portal.models.location import Location

try:
    # atom = Location(name='atom', url='https://ap:4000', type='external', priority=7, is_available=True, transfer_provider='http')
    atom = Location(name='atom', url='https://cai-murdoch.cai.uq.edu.au:4001', type='external', priority=7, is_available=True, transfer_provider='http')
    atom.save()
    print 'created Location: ' + str(atom)
except IntegrityError:
    print 'Location for atom provider already exists, continuing...'
