#!/usr/bin/python3
""" Compressed archive creation script """

from fabric.api import local
import time

def do_pack():
    """ Creates a compressed archive of web_static folder """
    try:
        local("mkdir -p versions")
        local(f"tar -cvzf versions/web_static_{time.strftime('%Y%m%d%H%M%S')}.tgz "
              f"web_static/")
        return (f"versions/web_static_{time.strftime('%Y%m%d%H%M%S')}.tgz")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None