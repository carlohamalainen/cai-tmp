FROM debian:jessie
MAINTAINER Carlo Hamalainen <carlo@carlo-hamalainen.net>

ADD         sources.list /etc/apt/sources.list
RUN         apt-get -qq update
RUN         apt-get -qqy dist-upgrade
RUN         apt-get -qqy install python python-dev cmake mercurial git ipython screen htop vim  \
                                 build-essential unzip cmake mercurial \
       	       	                 uuid-dev libcurl4-openssl-dev liblua5.1-0-dev \
       	       	                 libgoogle-glog-dev libgtest-dev libpng-dev \
       	       	                 libsqlite3-dev libssl-dev zlib1g-dev libdcmtk2-dev \
                                 libboost-all-dev libwrap0-dev libjsoncpp-dev

RUN         mkdir -p /opt
WORKDIR     /opt

ADD         Orthanc-0.8.0.tar.gz /opt/

RUN         mkdir /opt/OrthancBuild
WORKDIR     /opt/OrthancBuild

RUN         cmake -DALLOW_DOWNLOADS=ON \
                  -DUSE_SYSTEM_GOOGLE_LOG=OFF \
                  -DUSE_SYSTEM_MONGOOSE=OFF \
                  -DUSE_GTEST_DEBIAN_SOURCE_PACKAGE=ON \
                  -DENABLE_JPEG=OFF \
                  -DENABLE_JPEG_LOSSLESS=OFF \
                  /opt/Orthanc-0.8.0

RUN         make

# HTTP 
EXPOSE      8042

# DICOM
EXPOSE      4242

ADD         Configuration.json /opt/OrthancBuild/
CMD         ./Orthanc ./Configuration.json --verbose
