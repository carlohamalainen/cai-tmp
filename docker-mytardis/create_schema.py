import sys

sys.path.append('/opt/mytardis')
from append_django_paths import *

from django.db import IntegrityError
from tardis.tardis_portal.models import Schema
from tardis.tardis_portal.models.parameters import ParameterName

try:
    s = Schema(namespace='http://cai.uq.edu.au/schema/metadata/1', name='metadatablob', type=Schema.DATAFILE)
    s.save()

    p = ParameterName(schema_id=s.id, name='dump', full_name='Full dump of DICOM metadata.', data_type=ParameterName.STRING, is_searchable=True)
    p.save()
except IntegrityError:
    print 'Schema for metadatablob already exists.'
