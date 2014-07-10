Build the image:

    sudo docker build -t='carlo/mytardis_stable_debian_jessie' .

Run it, linking it against the atom provider:

    sudo docker run -i -t -p 0.0.0.0:3022:22 -p 0.0.0.0:8000:8000 -P --link ap:ap carlo/mytardis_stable_debian_jessie

Visit http://cai-murdoch.cai.uq.edu.au:8000

The admin account is username admin, password admin.

Now, inside the mytardis container, the url https://ap:4000 magically
connects to the atom provider in the other container!

For convenience, we map 3022 on the host to 22 in the container, and
ditto for 8000. We have sshd running on 3022 and the MyTards django
dev server runs on 8000.
