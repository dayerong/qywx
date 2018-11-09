#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import os
import sys

sys.path.append("..")
import system.jiradb as jiradb


class QueryCPT(object):
    def __init__(self):
        self.logger = web.ctx.environ['wsgilog.logger']
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, '../templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        rs = jiradb.get_undeploy_cpt()
        return self.render.querycpt(rs)


class Icon():
    def GET(self):
        raise web.seeother('/static/img/favicon.ico')
