#!/bin/bash

# Adapted from: https://github.com/novapost/docker-django-demo/blob/master/docs/index.rst

# export DJANGO_SETTINGS_MODULE=settings

# echo "[run] go to tardis folder"
# cd /opt/mytardis/tardis

echo "[run] syncdb"
./bin/django syncdb --noinput

echo "[run] create superuser"
echo "from django.contrib.auth.models import User
from tardis.tardis_portal.models import UserProfile
if not User.objects.filter(username='admin').count():
    u = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    UserProfile(user=u).save()
" | ./bin/django shell

echo "[run] runserver"
./bin/django runserver 0.0.0.0:8000
