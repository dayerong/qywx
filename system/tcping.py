#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


def portcheck(ip, port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rs = sock.connect_ex((ip, int(port)))
        if rs == 0:
            return "【%s:%s】 Port is open!" % (ip, port)
        elif rs == 111:
            return "【%s:%s】 Port is down!" % (ip, port)
        elif rs == 11:
            return "【%s】 IP is unreachable! " % ip
    except:
        return "【%s】 Name or service not known! " % ip
    sock.close()
