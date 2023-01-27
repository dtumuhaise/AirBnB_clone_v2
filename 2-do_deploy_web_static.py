#!/usr/bin/python3
""" distributes archive to webservers """

from fabric.api import *
import os


env.hosts = ['70942-web-01', '70942-web-02']


def do_deploy(archive_path):
    """ function to deploy """

    if not os.path.exists(archive_path):
        return False
    archive_name = os.path.basename(archive_path)
    archive_folder = archive_name.split(".")[0]
    put(archive_path, '/tmp/' + archive_name)
    run('mkdir -p /data/web_static/releases/' + archive_folder)
    run('tar -xzf /tmp/' + archive_name + ' -C /data/web_static\
        /releases/' + archive_folder)
    run('rm /tmp/' + archive_name)
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/' + archive_folder +
        ' /data/web_static/current')
    return True
