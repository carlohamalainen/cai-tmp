#!/usr/bin/env python

import os

os.chdir('/opt/mytardis')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

os.system('ln -s bin/django djangosettings.py')

import djangosettings
import sys
sys.path += djangosettings.sys.path

import os.path
sys.path.append(os.path.join(os.getcwd(), 'tardis'))

from django.db import IntegrityError
from tardis.tardis_portal.models.experiment import Experiment

import time

while True:
    for e in Experiment.objects.all():
        print 'Setting %s to be public (full access)' % (e.title,)
        e.public_access = Experiment.PUBLIC_ACCESS_FULL
        e.save()

    time.sleep(10)
