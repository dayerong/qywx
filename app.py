#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import web
import hashlib
from boot.qywx_api import QYWXapi
from boot.qywx_menu import CreatMenu
from boot.jira import ToInnerjira
from boot.inner_jira import Icon
from boot.inner_jira import JiraTable
from boot.querycpt import QueryCPT


import sys

# sys.path.append("..")
import logs.log as Mylog

urls = (
    '/jnks', 'QYWXapi',
    '/crmenu', 'CreatMenu',
    '/favicon.ico', 'Icon',
    '/jira', 'ToInnerjira',
    '/inner_jira', 'JiraTable',
    '/query_cpt', 'QueryCPT',
)

web.config.debug = False

if __name__ == '__main__':
    log = Mylog.Log
    app_root = os.path.dirname(__file__)
    templates_root = os.path.join(app_root, 'templates')
    render = web.template.render(templates_root)
    web.application(urls, globals()).run(log)
