Build the image:

    sudo docker build -t='carlo/mytardis01' .

Look at the new images:

    $ sudo docker images
    REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
    carlo/mytardis01    latest              c6bd020b14d1        2 minutes ago       713.2 MB
    ubuntu              utopic              58faa899733f        4 days ago          196 MB
    ubuntu              14.10               58faa899733f        4 days ago          196 MB
    ubuntu              precise             ea7d6801c538        10 days ago         127.4 MB
    ubuntu              12.04               ea7d6801c538        10 days ago         127.4 MB
    ubuntu              12.10               c5881f11ded9        2 weeks ago         172.1 MB
    ubuntu              quantal             c5881f11ded9        2 weeks ago         172.1 MB
    ubuntu              13.04               463ff6be4238        2 weeks ago         169.4 MB
    ubuntu              raring              463ff6be4238        2 weeks ago         169.4 MB
    ubuntu              saucy               195eb90b5349        2 weeks ago         184.6 MB
    ubuntu              13.10               195eb90b5349        2 weeks ago         184.6 MB
    ubuntu              latest              e54ca5efa2e9        2 weeks ago         276.1 MB
    ubuntu              trusty              e54ca5efa2e9        2 weeks ago         276.1 MB
    ubuntu              14.04               e54ca5efa2e9        2 weeks ago         276.1 MB
    ubuntu              lucid               3db9c44f4520        10 weeks ago        183 MB
    ubuntu              10.04               3db9c44f4520        10 weeks ago        183 MB

Run it, exposing the container's port 8000 as 8000 on localhost:

    $ sudo docker run -i -t -p 127.0.0.1:8000:8000 carlo/mytardis02
    [run] syncdb
    Syncing...
    Creating tables ...
    Installing custom SQL ...

    (snipped...)

    [run] runserver
    Validating models...

    0 errors found
    July 05, 2014 - 21:48:47
    Django version 1.5.5, using settings 'tardis.settings'
    Development server is running at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.

Navigate to http://localhost:8000 to see the django site.
