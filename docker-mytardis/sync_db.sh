#!/bin/bash

/usr/lib/postgresql/9.3/bin/postgres -D /var/lib/postgresql/9.3/main -c config_file=/etc/postgresql/9.3/main/postgresql.conf &

echo "=> Creating the tardis database"
RET=1
while [[ RET -ne 0 ]]; do
    sleep 5
    createdb tardis
    RET=$?
done

echo "=> Syncing django database"
RET=1
while [[ RET -ne 0 ]]; do
    sleep 5
    cd /opt/mytardis
    ./bin/django syncdb --noinput --migrate
    RET=$?
done

pg_ctl stop

echo "=> Done!"
