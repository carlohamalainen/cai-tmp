Build it:

    sudo docker build -t='carlo/atom-provider-01' .

Run it, naming it ap, and mount the carlo_brain directory as /opt/data, read-only:

    sudo docker run -i -t --rm -p 0.0.0.0:4000:4000 -P --name ap -v /export/scratch02/carlo_brain:/opt/data:ro carlo/atom-provider-01

This opens https://localhost:4000 so you can view the atom feed.

And it names it "ap" so we can link it to the MyTardis container and
from that container, the url https://ap:4000 will refer to the atom feed.
