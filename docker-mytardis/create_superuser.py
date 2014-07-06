import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.contrib.auth.management.commands import changepassword
from django.core import management

# Drop the DB and recreate it
# os.system('echo drop schema myDB; | mysql --user=root --password=root')
# os.system('echo create schema myDB; | mysql --user=root --password=root')

# Run the syncdb
# management.call_command('syncdb', interactive=False)

management.call_command('createsuperuser', interactive=False, username='superuser', email='superuser@example.com')
command = changepassword.Command()
command._get_pass = lambda *args: 'password'
command.execute('superuser')
