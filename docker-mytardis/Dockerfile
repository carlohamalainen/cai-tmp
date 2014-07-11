FROM debian:jessie
MAINTAINER Carlo Hamalainen <carlo@carlo-hamalainen.net>

ADD         sources.list /etc/apt/sources.list
RUN         apt-get -qq update
RUN         apt-get -qqy dist-upgrade
RUN         apt-get -qqy install python python-dev libpq-dev libssl-dev libsasl2-dev libldap2-dev libxslt1.1 libxslt1-dev python-libxslt1 libexiv2-dev git libgraphviz-dev git ipython screen htop imagemagick vim dcmtk

RUN         mkdir -p /opt
WORKDIR     /opt

RUN         git clone git://github.com/mytardis/mytardis.git
RUN         git clone git://github.com/carlohamalainen/mytardis-app-atom.git /opt/mytardis/tardis/apps/atom

ADD         /settings.py                            /opt/mytardis/tardis/
ADD         /buildout-dev.cfg                       /opt/mytardis/
ADD         /create_superuser.py                    /opt/mytardis/
ADD         /create_admin.py                        /opt/mytardis/
ADD         /create_atom_location.py                /opt/mytardis/
ADD         /testing_set_all_experiments_public.py  /opt/mytardis/
RUN         chmod +x /opt/mytardis/testing_set_all_experiments_public.py

WORKDIR     /opt/mytardis

RUN         python bootstrap.py -v 1.7.0
RUN         ./bin/buildout -c buildout-dev.cfg

RUN         ./bin/django syncdb --noinput --migrate

RUN         python create_superuser.py  
RUN         python create_admin.py
RUN         python create_atom_location.py

# http://stackoverflow.com/a/11788659/3659845
# PYTHONPATH='/opt/mytardis':`ls -d -1 /opt/mytardis/eggs/* | tr '\n' ':'`

ADD run.sh /opt/mytardis/
ADD run_celery.sh /opt/mytardis/
RUN chmod +x /opt/mytardis/run*sh

EXPOSE 8000

RUN         mkdir /root/.ssh
ADD         authorized_keys /root/.ssh/
RUN         chmod 700 /root/.ssh
RUN         chmod 600 /root/.ssh/authorized_keys

RUN echo 'root:root' | chpasswd
RUN apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd ; chmod -rx /var/run/sshd
# http://stackoverflow.com/questions/2419412/ssh-connection-stop-at-debug1-ssh2-msg-kexinit-sent
RUN rm -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
# Bad security, add a user and sudo instead!
RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
# http://stackoverflow.com/questions/18173889/cannot-access-centos-sshd-on-docker
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config

# For celery, should use a different account
ENV C_FORCE_ROOT YES

RUN apt-get install -y supervisor
ADD supervisord.conf /etc/supervisord.conf
EXPOSE 3022 22


# FIXME Fiddling with this so at the end of the file for the moment.
ADD         /dicompng.py                            /opt/mytardis/tardis/tardis_portal/filters/

ADD         /create_schema.py                        /opt/mytardis/
RUN python create_schema.py

# Sqlite database for MyTardis is stored here:
VOLUME      /sqlite

# MyTardis file store, staging area, etc:
# VOLUME      /opt/mytardis/var

CMD /usr/bin/supervisord -c /etc/supervisord.conf
