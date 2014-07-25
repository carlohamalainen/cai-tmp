#!/usr/bin/env python

import sys

sys.path.append('/opt/mytardis')
from append_django_paths import *

from tardis.tardis_portal.models.experiment import Experiment

import time

while True:
    for e in Experiment.objects.all():
        print 'Setting %s to be public (full access)' % (e.title,)
        e.public_access = Experiment.PUBLIC_ACCESS_FULL
        e.save()

    time.sleep(10)
