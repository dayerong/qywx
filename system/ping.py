#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands


def checkping(ip):
    cmd = 'ping -c 1 -w 2 ' + ip
    rs = commands.getstatusoutput(cmd)[0]
    return rs
