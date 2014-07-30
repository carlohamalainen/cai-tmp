# Docker container for MyTardis

Build the image:

    sudo docker build -t='user/mytardis_stable_debian_jessie' .

Run it:

    sudo docker run -i -t --rm -p 0.0.0.0:3022:22 -p 0.0.0.0:8000:8000 -P \
    -v /data/home/uqchamal/scratch-docker-mytardis:/scratch \
    -v /export/scratch02/mytardis/staging:/mytardis_staging \
    -v /export/scratch02/mytardis/store:/mytardis_store \
    -v /mnt:/other \
    user/mytardis_stable_debian_jessie

Visit http://cai-murdoch.cai.uq.edu.au:8000

**The admin account is username admin, password admin. In production,
use a sensible password or pwgen.**

Convenient ssh command to connect to the container:

    ssh -t -o NoHostAuthenticationForLocalhost=yes -p 3022 root@localhost

Look for errors in the logs:

    grep -i error /opt/mytardis/*log /var/log/supervisor/*log

# TODO

Move Postgresql database onto a volume for persistence.

# Notes

Beware that ```/var/lib/docker``` can get large. Put this on a mount
point with enough free space.

# Timing

* CAI 3T, samba mount, 6 hours 10 minutes to import
```/mnt/12014_MITIITM```. Each directory of DICOM files converted to
MNC, thumbnails generated, and MNC metadata extracted.


