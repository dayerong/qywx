#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssh as myssh


def restart_ss():
    ip = 'x.x.x.x'
    port = 22
    username = 'user'
    password = 'password'
    execmd = 'sudo /opt/tools/restart_ss.sh'
    restart_ss = myssh.ssh_exec_command(ip, port, username, password, execmd)
    return restart_ss


def check_ss():
    ip = 'x.x.x.x'
    port = 22
    username = 'user'
    password = 'password'
    execmd = ' ps -ef |grep -E "UID|servers" |grep -v grep'
    check_ss = myssh.ssh_exec_command(ip, port, username, password, execmd)
    return check_ss
