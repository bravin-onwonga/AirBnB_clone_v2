#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static using do_pack
"""

import os
from fabric import task
from datetime import datetime


@task
def do_pack(c):
    """
    Function that connect to the servers and archives the content
    """

    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + time_now + ".tgz"
    res = c.local('tar -czf {} web_static'.format(filename))

    if res.ok:
        path = os.path.getsize(filename)
        return (path)
    else:
        return None


if __name__ == "__main__":
    from fabric import Connection
    c = Connection('localhost')
    do_pack(c)
