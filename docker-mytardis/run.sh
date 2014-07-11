#!/bin/bash

# Adapted from: https://github.com/novapost/docker-django-demo/blob/master/docs/index.rst

# export DJANGO_SETTINGS_MODULE=settings


# If we can see the database on the volume, use that instead.
#if [ ! -f /sqlite/tardis_db ]; then
#    cp /opt/mytardis/tardis_db /sqlite/tardis_db
#fi

#mv /opt/mytardis/tardis_db{,_original}
#ln -s /sqlite/tardis_db /opt/mytardis/tardis_db

cd /opt/mytardis

echo "[run] syncdb"
./bin/django syncdb --noinput

python create_superuser.py  
python create_admin.py
python create_atom_location.py
python create_schema.py

echo "[run] runserver"
./bin/django runserver 0.0.0.0:8000
