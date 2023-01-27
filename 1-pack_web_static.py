#!/usr/bin/python3
""" generates .tgz archive """

from fabric.api import local, settings, lcd
from datetime import datetime


def do_pack():
    """ function to create the archive """

    with settings(warn_only=True):
        if local("test -d versions").failed:
            local("mkdir versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    with lcd("web_static"):
        local("tar -czf ../versions/{} .".format(archive_name))
    return ("versions/{}".format(archive_name))
