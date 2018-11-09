#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import types


def md5(str):
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''
