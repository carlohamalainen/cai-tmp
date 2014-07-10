import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

os.system('ln -s bin/django djangosettings.py')

import djangosettings
import sys
sys.path += djangosettings.sys.path

import os.path
sys.path.append(os.path.join(os.getcwd(), 'tardis'))

from django.contrib.auth.models import User
from tardis.tardis_portal.models import UserProfile

if not User.objects.filter(username='admin').count():
    u = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    UserProfile(user=u).save()
