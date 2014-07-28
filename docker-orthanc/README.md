# Docker container for Orthanc

Build it:

    sudo docker build -t='user/orthanc' .

Run it:

    sudo docker run -i -t --rm -p 0.0.0.0:8042:8042 -p 0.0.0.0:4242:4242 user/orthanc

Import a dataset:

    ./ImportDicomFiles.py localhost 8042 /mnt/CARLO_HAMALAINEN/mytardis_ingestion_testing/

    ./ImportDicomFiles.py localhost 8042 /export/scratch02/carlo_brain_just_t1
