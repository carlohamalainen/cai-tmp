#!/bin/bash

# Adapted from: https://github.com/novapost/docker-django-demo/blob/master/docs/index.rst

# export DJANGO_SETTINGS_MODULE=settings

cd /opt/mytardis

echo "[run] syncdb"
./bin/django syncdb --noinput

echo "[run] runserver"
./bin/django runserver 0.0.0.0:8000
