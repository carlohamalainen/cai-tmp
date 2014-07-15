#!/bin/bash

exec su postgres -c "/usr/lib/postgresql/9.3/bin/postgres -D /var/lib/postgresql/9.3/main -c config_file=/etc/postgresql/9.3/main/postgresql.conf" &

echo "=> Syncing django database"
RET=1
while [[ RET -ne 0 ]]; do
    sleep 1
    cd /opt/mytardis
    ./bin/django syncdb --noinput
    RET=$?
done

# Assume from here on that the database is up...
set -e

cd /opt/mytardis

./bin/django syncdb --noinput
./bin/django migrate
./bin/django schemamigration tardis_portal --auto
./bin/django migrate tardis_portal

echo "=> Done!"
