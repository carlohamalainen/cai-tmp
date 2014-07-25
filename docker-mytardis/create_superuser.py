import sys

sys.path.append('/opt/mytardis')
from append_django_paths import *

from django.contrib.auth.management.commands import changepassword
from django.core import management

management.call_command('createsuperuser', interactive=False, username='superuser', email='superuser@example.com')
command = changepassword.Command()
command._get_pass = lambda *args: 'password'
command.execute('superuser')


