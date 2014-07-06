FROM ubuntu
MAINTAINER Carlo Hamalainen <carlo@carlo-hamalainen.net>

RUN         apt-get -qq update
RUN         apt-get -qqy install python python-dev libpq-dev libssl-dev libsasl2-dev libldap2-dev libxslt1.1 libxslt1-dev python-libxslt1 libexiv2-dev git libgraphviz-dev git ipython screen htop imagemagick vim

RUN         mkdir -p /opt
WORKDIR     /opt

RUN         git clone -b develop git://github.com/mytardis/mytardis.git

ADD         /settings.py /opt/mytardis/tardis/
ADD         /buildout-dev.cfg /opt/mytardis/
ADD         /create_superuser.py /opt/mytardis/

WORKDIR     /opt/mytardis

RUN         python bootstrap.py -v 1.7.0
RUN         ./bin/buildout -c buildout-dev.cfg

RUN         ./bin/django syncdb --noinput --migrate

# http://stackoverflow.com/a/11788659/3659845
# PYTHONPATH='/opt/mytardis':`ls -d -1 /opt/mytardis/eggs/* | tr '\n' ':'`

ADD run.sh /opt/mytardis/
RUN chmod +x /opt/mytardis/run.sh

EXPOSE 8000

CMD /opt/mytardis/run.sh
