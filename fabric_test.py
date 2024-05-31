#!/usr/bin/python3
from fabric import Connection

with Connection(host='100.25.141.192',
                user='ubuntu',
                connect_kwargs={
                    'key_filename': '/home/bravin/.ssh/id_rsa',
                },
                ) as c:
                    c.put('0-setup_web_static.sh', remote='/home/ubuntu')
