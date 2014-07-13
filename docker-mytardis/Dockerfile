FROM        debian:jessie
MAINTAINER  Carlo Hamalainen <carlo@carlo-hamalainen.net>

ADD         sources.list /etc/apt/sources.list
RUN         apt-get -qq update
RUN         apt-get -qqy dist-upgrade
RUN         apt-get -qqy install python python-dev libpq-dev libssl-dev libsasl2-dev   \
                                 libldap2-dev libxslt1.1 libxslt1-dev python-libxslt1  \
                                 libexiv2-dev git libgraphviz-dev git ipython screen   \
                                 htop imagemagick vim dcmtk openssh-server supervisor  \
                                 pwgen libpq-dev python-dev python-software-properties \
                                 software-properties-common python-psycopg2

RUN         DEBIAN_FRONTEND=noninteractive apt-get -y install postgresql postgresql-contrib 

ADD         /postgresql.conf /etc/postgresql/9.3/main/postgresql.conf

USER        postgres
RUN         /etc/init.d/postgresql start && \
                psql --command "CREATE USER admin WITH SUPERUSER PASSWORD 'admin';" && \
                createdb -O admin admin

USER        root

RUN         mkdir -p /opt
WORKDIR     /opt

RUN         git clone git://github.com/mytardis/mytardis.git
RUN         git clone git://github.com/carlohamalainen/mytardis-app-atom.git /opt/mytardis/tardis/apps/atom

# FIXME
RUN         sed -i 's/max_length=50/max_length=100/g' /opt/mytardis/tardis/tardis_portal/models/access_control.py

ADD         settings.py                             /opt/mytardis/tardis/
ADD         buildout-dev.cfg                        /opt/mytardis/
ADD         create_superuser.py                     /opt/mytardis/
ADD         create_admin.py                         /opt/mytardis/
ADD         create_atom_location.py                 /opt/mytardis/
ADD         testing_set_all_experiments_public.py   /opt/mytardis/
ADD         run.sh                                  /opt/mytardis/
ADD         run_celery.sh                           /opt/mytardis/
ADD         create_postgres_tardis.sh               /opt/mytardis/
ADD         migrate_and_sync.sh                     /opt/mytardis/
ADD         supervisord.conf                        /etc/supervisord.conf
ADD         dicom                                   /opt/mytardis/tardis/tardis_portal/filters/dicom
ADD         create_schema.py                        /opt/mytardis/


RUN         chmod +x /opt/mytardis/*.sh
RUN         chmod +x /opt/mytardis/testing_set_all_experiments_public.py

WORKDIR     /opt/mytardis

RUN         python bootstrap.py -v 1.7.0
RUN         ./bin/buildout -c buildout-dev.cfg

# http://stackoverflow.com/a/11788659/3659845
# PYTHONPATH='/opt/mytardis':`ls -d -1 /opt/mytardis/eggs/* | tr '\n' ':'`

EXPOSE 8000

RUN         mkdir /root/.ssh
ADD         authorized_keys /root/.ssh/
RUN         chmod 700 /root/.ssh
RUN         chmod 600 /root/.ssh/authorized_keys

RUN         mkdir -p  /var/run/sshd
RUN         chmod -rx /var/run/sshd
RUN         rm -f /etc/ssh/ssh_host_rsa_key
RUN         ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key

# Weird bug with ssh, have to disable PAM otherwise we get logged out immediately.
# http://stackoverflow.com/questions/18173889/cannot-access-centos-sshd-on-docker
RUN         sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN         sed -ri 's/#UsePAM no/UsePAM no/g'   /etc/ssh/sshd_config

# For celery, should use a different account
ENV C_FORCE_ROOT YES

EXPOSE 3022 22

# Sqlite database for MyTardis is stored here:
# VOLUME      /sqlite

# Stick logs on a volume too.
# VOLUME      /var/log

# MyTardis file store, staging area, etc:
# VOLUME      /opt/mytardis/var

RUN         /opt/mytardis/create_postgres_tardis.sh

RUN         /opt/mytardis/migrate_and_sync.sh

CMD         /usr/bin/supervisord -c /etc/supervisord.conf

#CMD         /usr/sbin/sshd -D
