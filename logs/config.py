#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging

# file = "../logs/webpy.log"
file = "./logs/webpy.log"
logformat = "[%(asctime)s][%(filename)s:%(funcName)s][%(levelname)s-%(message)s]"
datefmt = "%Y-%m-%d %H:%M:%S"
loglevel = logging.DEBUG
interval = "d"
backups = 7
