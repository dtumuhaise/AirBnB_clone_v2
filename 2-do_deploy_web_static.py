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

    run('mkdir -p /data/web_static/releases/{}'.format(archive_name))

    run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
        .format(archive_name, archive_name))

    run('rm /tmp/{}.tgz'.format(archive_name))

    run(('mv /data/web_static/releases/{}/web_static/* ' +
        '/data/web_static/releases/{}/')
        .format(archive_name, archive_name))

    run('rm -rf /data/web_static/current')

    run('rm -rf /data/web_static/releases/{}/web_static'
        .format(archive_name))

    run('ln -s /data/web_static/releases/{}/' +
        ' /data/web_static/current'.format(archive_name))
    return True
