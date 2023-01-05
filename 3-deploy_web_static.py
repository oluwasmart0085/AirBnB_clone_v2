#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""

from fabric.api import *
from datetime import datetime
from os.path import isfile


env.user = 'ubuntu'
env.hosts = ['3.239.86.158', '34.239.166.29']


def do_pack():
    """.tgz generator function"""
    date_now = datetime.now()
    file_name = 'web_static_{}{}{}{}{}{}.tgz'.format(
        str(date_now.year), str(date_now.month), str(date_now.day),
        str(date_now.hour), str(date_now.minute), 
        str(date_now.second))
    local("mkdir -p  versions")
    archive = local('tar -cvzf versions/{} web_static'.format(
        file_name))
    if archive.failed:
        return None
    return 'versions/{}'.format(file_name)


def do_deploy(archive_path):
    """ Distribute an archive to the web servers """
    if not isfile(archive_path):
        return False
    put('{}'.format(archive_path), '/tmp/')
    archive__ = archive_path.split('.')
    archive_ = archive__[0].split("/")
    archive = archive_[1]
    run('mkdir -p /data/web_static/releases/{}/'.format(archive))
    run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
        .format(archive, archive))
    run('rm /tmp/{}.tgz'.format(archive))
    run('mv /data/web_static/releases/{}/web_static/* '.format(archive)
        + '/data/web_static/releases/{}/'.format(archive))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(archive))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(archive))
    print('New version deployed!')
    return True


def deploy():
    """ Create and distribute an archive to the web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
