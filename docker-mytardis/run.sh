#!/bin/bash

# Adapted from: https://github.com/novapost/docker-django-demo/blob/master/docs/index.rst

cd /opt/mytardis

echo "[run] syncdb"

echo "=> Waiting for postgresql to come online"
RET=1
while [[ RET -ne 0 ]]; do
    echo "=> sleeping 5 seconds..."
    sleep 1
    ./bin/django syncdb --noinput --migrate
    RET=$?
done

set -e

python create_superuser.py  
python create_admin.py
python create_atom_location.py
python create_schema.py

echo "[run] runserver"
./bin/django runserver 0.0.0.0:8000
