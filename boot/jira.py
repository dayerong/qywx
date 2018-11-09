#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import os
import sys


class ToInnerjira():
    def __init__(self):
        self.logger = web.ctx.environ['wsgilog.logger']
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, '../templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        raise web.seeother('http://api.my.com.cn/inner_jira')
