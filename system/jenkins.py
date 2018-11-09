#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands


def deploy_e3():
    cmd = 'su - jenkins -c "ssh -l jenkins -p 53802 x.x.x.x build E3系统代码部署 -p Choice=Deploy"'
    rs = commands.getstatusoutput(cmd)[0]
    return rs

def deploy_cpt():
    cmd = 'su - jenkins -c "ssh -l jenkins -p 53802 x.x.x.x build CPT报表部署 -p Choice=Deploy"'
    rs = commands.getstatusoutput(cmd)[0]
    return rs