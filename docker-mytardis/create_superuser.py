import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

os.system('ln -s bin/django djangosettings.py')

import djangosettings
import sys
sys.path += djangosettings.sys.path

import os.path
sys.path.append(os.path.join(os.getcwd(), 'tardis'))



from django.contrib.auth.management.commands import changepassword
from django.core import management

management.call_command('createsuperuser', interactive=False, username='superuser', email='superuser@example.com')
command = changepassword.Command()
command._get_pass = lambda *args: 'password'
command.execute('superuser')


