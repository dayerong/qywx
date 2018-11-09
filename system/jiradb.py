#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import MySQLdb
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

""" 数据库连接参数 """
config = {
    'host': 'x.x.x.x',
    'port': 3306,
    'user': 'user',
    'passwd': 'password',
    'db': 'jiradb',
    'charset': 'utf8'
}


def get_owner_jira(jirauser):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select issuenum,SUMMARY,REPORTER,UPDATED  from jiraissue where assignee = \'%s\' and RESOLUTION is null" % jirauser
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    finally:
        cursor.close()
        conn.close()


def get_undeploy_cpt():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = "select ISSUENUM,SUMMARY,AUTHOR,REALFILE from cpt_file_map where DEPLOY_STATUS='N'"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    finally:
        cursor.close()
        conn.close()
