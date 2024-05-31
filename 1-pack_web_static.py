#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static using do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function that connect to the servers and archives the content

    Returns
        - path to file if successful
        - otherwise None
    """
    local('sudo mkdir -p versions')

    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_" + time_now + ".tgz"
    res = local('sudo tar -czf {} web_static'.format(filename))

    if res.success:
        return (filename)
    else:
        return None


if __name__ == "__main__":
    do_pack()
