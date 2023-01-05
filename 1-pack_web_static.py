#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """.tgz generator function"""
    date_now = datetime.now()
    file_name = 'web_static_{}{}{}{}{}{}.tgz'.format(
        str(date_now.year), str(date_now.month), 
        str(date_now.day),
        str(date_now.hour), str(date_now.minute),
        str(date_now.second))
    local("mkdir -p  versions")
    archive = local('tar -cvzf versions/{} web_static'.format(
        file_name))
    if archive.failed:
        return None
    return 'versions/{}'.format(file_name)
