#!/usr/bin/python3
"""
Distributes archived file to the web server based on the file 1-pack_web_static.py
"""

from fabric import *
import os

env.hosts = ['100.25.141.192', '54.237.117.188']
env.key_filename = '/home/bravin/.ssh/id_rsa'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Function to distributes archived file to the web server
    Extract and creates a symblic link to the extracted folder

    Parameter:
        - archive_path: path to archive
    Returns:
        - True: success
        - False: failure
    """
    if not os.path.isfile(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_filename = archive_path.split('/')[1]
        archive = archive_filename.split('.')[0]
        destination = '/data/web_static/releases/{}'.format(archive)
        run('mkdir -p {}'.format(destination))
        run('tar xf /tmp/{} --directory={}'.format(archive_filename, destination))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}/web_static/* {}'.format(destination, destination))
        run('rm -rf {}/web_static'.format(destination))
        run('rm -rf /data/web_static/current')
        run('ln -sf {} /data/web_static/current'.format(destination))
        return True
    except Exception:
        return False
