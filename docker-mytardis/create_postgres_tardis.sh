#!/bin/bash

exec su postgres -c "/usr/lib/postgresql/9.3/bin/postgres -D /var/lib/postgresql/9.3/main -c config_file=/etc/postgresql/9.3/main/postgresql.conf" &

echo "=> Creating the tardis database"
RET=1
while [[ RET -ne 0 ]]; do
    sleep 1
    exec su postgres -c "createdb tardis"
    RET=$?
done

echo "=> Done!"
