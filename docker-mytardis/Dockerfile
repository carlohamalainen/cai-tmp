FROM        debian:jessie
MAINTAINER  Carlo Hamalainen <carlo@carlo-hamalainen.net>

# Update and install packages.
ADD         sources.list /etc/apt/sources.list
RUN         apt-get -qq update
RUN         apt-get -qqy dist-upgrade
RUN         apt-get -qqy install python python-dev libpq-dev libssl-dev libsasl2-dev   \
                                 libldap2-dev libxslt1.1 libxslt1-dev python-libxslt1  \
                                 libexiv2-dev git libgraphviz-dev git ipython screen   \
                                 htop imagemagick vim dcmtk openssh-server supervisor  \
                                 pwgen libpq-dev python-dev python-software-properties \
                                 software-properties-common python-psycopg2 pyflakes   \
                                 tcsh make vim-gtk minc-tools python-pip

RUN         pip install requests --upgrade

RUN         pip install pydicom
RUN         pip install pynetdicom

RUN         DEBIAN_FRONTEND=noninteractive apt-get -qqy install postgresql postgresql-contrib

# Sane vim environment.
RUN         mkdir /root/.vim
ADD         vim/.vimrc   /root/.vimrc
ADD         vim/autoload /root/.vim/autoload
ADD         vim/bundle   /root/.vim/bundle

WORKDIR     /root/.vim/bundle/vimproc.vim
RUN         make

# Sane bash settings.
ADD         bashrc-extra /root/.bashrc-extra
RUN         echo 'source /root/.bashrc-extra' >> /root/.bashrc

# SSH access using the authorized_keys file (not in the git repo).
RUN         mkdir /root/.ssh
ADD         authorized_keys /root/.ssh/
RUN         chmod 700 /root/.ssh
RUN         chmod 600 /root/.ssh/authorized_keys

# SSH daemon needs host keys to be generated.
RUN         mkdir -p  /var/run/sshd
RUN         chmod -rx /var/run/sshd
RUN         rm -f /etc/ssh/ssh_host_rsa_key
RUN         ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key

# Weird bug with SSH, have to disable PAM otherwise we get logged out immediately.
# http://stackoverflow.com/questions/18173889/cannot-access-centos-sshd-on-docker
RUN         sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN         sed -ri 's/#UsePAM no/UsePAM no/g'   /etc/ssh/sshd_config

# Set up the postgresql admin user with password admin.
# FIXME Change this to use pwgen?
ADD         /postgresql.conf /etc/postgresql/9.3/main/postgresql.conf
USER        postgres
RUN         /etc/init.d/postgresql start && \
                psql --command "CREATE USER admin WITH SUPERUSER PASSWORD 'admin';" && \
                createdb -O admin admin
USER        root

# Install MyTardis.
RUN         mkdir -p /opt
WORKDIR     /opt

#RUN         git clone git://github.com/mytardis/mytardis.git
ADD         mytardis-86b63c1d1648ee19bceb1e71039abe733fea8038  /opt/mytardis

#RUN         git clone git://github.com/carlohamalainen/mytardis-app-atom.git /opt/mytardis/tardis/apps/atom
ADD         mytardis-app-atom-b384213113e5164937595413f23a11b28570e037 /opt/mytardis/tardis/apps/atom

# RUN         git clone -b enhanced_storage_backend https://github.com/grischa/mytardis.git
# RUN         git clone -b develop git://github.com/mytardis/mytardis.git

# Dodgy patch: allow longer usernames.
# Note: turning this off means that create_and_sync.sh may fail since there
# will be no schema to migrate ("Installed 0 object(s) from 0 fixture(s); Nothing seems to have changed.").
RUN         sed -i 's/max_length=50/max_length=100/g' /opt/mytardis/tardis/tardis_portal/models/access_control.py

ADD         buildout-dev.cfg /opt/mytardis/
WORKDIR     /opt/mytardis
RUN         python bootstrap.py -v 1.7.0
RUN         ./bin/buildout -c buildout-dev.cfg
WORKDIR     /opt

ADD         settings.py                             /opt/mytardis/tardis/
ADD         append_django_paths.py                  /opt/mytardis/
ADD         create_superuser.py                     /opt/mytardis/
ADD         create_admin.py                         /opt/mytardis/
ADD         create_atom_location.py                 /opt/mytardis/
ADD         testing_set_all_experiments_public.py   /opt/mytardis/
ADD         run.sh                                  /opt/mytardis/
ADD         run_celery.sh                           /opt/mytardis/
ADD         create_postgres_tardis.sh               /opt/mytardis/
ADD         migrate_and_sync.sh                     /opt/mytardis/
ADD         supervisord.conf                        /etc/supervisord.conf
#ADD         dicom                                   /opt/mytardis/tardis/tardis_portal/filters/dicom
ADD         create_schema.py                        /opt/mytardis/

RUN         chmod +x /opt/mytardis/*.sh


WORKDIR     /opt/mytardis
RUN         ln -s bin/django djangosettings.py

WORKDIR     /opt

# FIXME For testing, this script sets all experiments to be public. Disable for
# production systems.
RUN         chmod +x /opt/mytardis/testing_set_all_experiments_public.py

# MyTardis is on port 8000.
EXPOSE 8000

# ssh
EXPOSE 22

# pynetdicom server
EXPOSE 5000

# Sqlite database for MyTardis is stored here:
# VOLUME      /sqlite

# Stick logs on a volume too.
# VOLUME      /var/log

# MyTardis file store, staging area, etc:
# VOLUME      /opt/mytardis/var

VOLUME      /mytardis_store
VOLUME      /mytardis_staging

# Temp space for development.
VOLUME      /scratch

# Create the 'tardis' database.
RUN         /opt/mytardis/create_postgres_tardis.sh

# Migrate and sync the django models.
RUN         /opt/mytardis/migrate_and_sync.sh

RUN         rmdir /opt/mytardis/var/store
RUN         ln -s /mytardis_store/ /opt/mytardis/var/store

RUN         rmdir /opt/mytardis/var/staging
RUN         ln -s /mytardis_staging/ /opt/mytardis/var/staging

VOLUME      /other

# Run supervisor - this loads MyTardis, celery, etc.
CMD         /usr/bin/supervisord -c /etc/supervisord.conf

# For testing, just load ssh.
#CMD         /usr/sbin/sshd -D
