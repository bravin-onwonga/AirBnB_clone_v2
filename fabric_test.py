#!/usr/bin/python3
from fabric import Connection

with Connection(host='54.237.117.188',
                user='ubuntu',
                connect_kwargs={
                    'key_filename': '/home/bravin/.ssh/id_rsa',
                },
                ) as c:
                    """ archive_path = 'versions/web_static_20240531160711.tgz'
                    c.put(archive_path, '/tmp/')
                    archive_filename = archive_path.split('/')[1].split('.')[0]
                    destination = '/data/web_static/releases/{}'.format(archive_filename)
                    c.run('mkdir -p {}'.format(destination))
                    c.run('tar xf /tmp/{}.tgz --directory={}'.format(archive_filename, destination))
                    c.run('rm /tmp/{}.tgz'.format(archive_filename))
                    c.run('mv {}/web_static/* {}'.format(destination, destination))
                    c.run('rm -rf {}/web_static'.format(destination))
                    c.run('rm -rf /data/web_static/current')
                    c.run('ln -sf {} /data/web_static/current'.format(destination)) """
                    c.put('0-setup_web_static.sh', '/home/ubuntu/')
