#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssh as myssh


def deploy():
    ip = 'x.x.x.x'
    port = 22
    username = 'root'
    password = 'password'
    execmd = '/usr/local/bin/python2.7 /opt/cpt/cpt.py'
    cpt_deploy = myssh.ssh_exec_command(ip, port, username, password, execmd)
    status = cpt_deploy.split('\n')[0]
    return status
