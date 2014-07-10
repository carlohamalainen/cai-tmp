# https://github.com/wettenhj/atom-dataset-provider

FROM debian:jessie
MAINTAINER Carlo Hamalainen <carlo@carlo-hamalainen.net>

ADD         sources.list /etc/apt/sources.list
RUN         apt-get -qq update
RUN         apt-get -qqy dist-upgrade
RUN         apt-get -qqy install python python-dev git ipython screen htop vim npm

# Debian provides nodejs, everyone else expects node.
run         ln -s /usr/bin/nodejs /usr/local/bin/node

RUN         mkdir /opt || echo '/opt already exists...'
WORKDIR     /opt

RUN         git clone https://github.com/wettenhj/atom-dataset-provider.git

WORKDIR     /opt/atom-dataset-provider

RUN         npm install


RUN mkdir /opt/atom-dataset-provider/keys
ADD server.key /opt/atom-dataset-provider/keys/
ADD server.crt /opt/atom-dataset-provider/keys/

ADD         feed.atom lib/atom-dataset-provider/templates/feed.atom

EXPOSE 4000

# CMD bin/atom-dataset-provider -d /opt/data -p 4000 --group-pattern '/^/opt/data/([^/]+/(?:mytardis)+/[^/]+/[^/]+/)/'
#
#                                                                                  ^          ^        ^     ^
#                                                                                  |          |        |     |
#                                                                                  |          |        |     |
#                                                                                  user       |        |     |
#                                                                                         mytardis     |     |
#                                                                                                    exp     |
#                                                                                                         dataset
#
#    which matches files with the path:
#
#    /opt/data/<user>/mytardis/<experiment>/<dataset>/<filename>

CMD bin/atom-dataset-provider -d /opt/data -p 4000 --group-pattern '/^/opt/data/([^/]+/[^/]+/[^/]+/[^/]+/)/'

# └── CH_14_07_09-10_17_55-STD-1_3_12_2_1107_5_2_34_18975
#     └── CH_14_07_09-10_17_55-STD-1_3_12_2_1107_5_2_34_18975
#         └── RESEARCH_KIERAN_20140709_101928_062000
#             ├── AAHSCOUT_32CH_0001
#             ├── AAHSCOUT_32CH_MPR_0002
#             ├── GRE_4P0_0020
#             ├── GRE_4P0_0021
#             ├── GRE_ME_0P75_T2STAR_0019
#             ├── GRE_ME_1P0_T2STAR_0018
#             ├── INLINE_MORPHO_RESULTS_0008
#             ├── MP2RAGE-WIP900_1_0ISO_7T_INV1_0006
#             ├── MP2RAGE-WIP900_1_0ISO_7T_INV2_0007
#             ├── MP2RAGE-WIP900_1_0ISO_7T_T1_IMAGES_0003
#             ├── MP2RAGE-WIP900_1_0ISO_7T_UNI-DEN_0004
#             ├── MP2RAGE-WIP900_1_0ISO_7T_UNI-DEN_LABELIM_0010
#             ├── MP2RAGE-WIP900_1_0ISO_7T_UNI-DEN_SKULLSTRIP_0009
#             ├── MP2RAGE-WIP900_1_0ISO_7T_UNI_IMAGES_0005
#             ├── PHOENIXZIPREPORT_0099
#             ├── SUB_S11-S12_1_0100
#             ├── SUB_S13-S14_1_0101
#             ├── SUB_S13-S15_1_0102
#             ├── SUB_S13-S16_1_0103
#             ├── SUB_S13-S17_1_0104
#             ├── UTE_20000RV_2ECHOS_P75ISO_0011
#             ├── UTE_20000RV_2ECHOS_P75ISO_0012
#             ├── UTE_20000RV_5ECHOS_P93ISO_0013
#             ├── UTE_20000RV_5ECHOS_P93ISO_0014
#             ├── UTE_20000RV_5ECHOS_P93ISO_0015
#             ├── UTE_20000RV_5ECHOS_P93ISO_0016
#             └── UTE_20000RV_5ECHOS_P93ISO_0017

