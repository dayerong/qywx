#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import xml.etree.ElementTree as ET
import urllib2
import json


# 自定义菜单
class CreatMenu:
    def __init__(self):
        self.corpid = "your_id"
        self.corpsecret = "your_secret"
        self.agentid = "1000003"

    def GET(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (self.corpid, self.corpsecret)
        response = urllib2.urlopen(url)
        html = response.read()
        tokeninfo = json.loads(html)
        token = tokeninfo['access_token']
        post = '''
 {
     "button":[
     {
          "name":"应用发布",
          "sub_button":[
            {
                "type":"click",
                "name":"E3系统部署",
                "key":"e3_deploy"
            },
            {
                "type":"click",
                "name":"CPT报表部署",
                "key":"cpt_deploy"
            },
            {
                "type":"click",
                "name":"SCM系统部署",
                "key":"scm_deploy"
            }
          ]
      },
      {
          "name":"日常运维",
          "sub_button":[
            {
                "type":"view",
                "name":"我的JIRA",
                "url":"http://api.my.com.cn/jira"
            },
            {
                "type":"view",
                "name":"查询未发布CPT",
                "url":"http://api.my.com.cn/query_cpt"
            },
            {
                "type":"click",
                "name":"重启ShadowSocks",
                "key":"ss_restart"
            }
          ]
      },
      {
          "type":"view",
           "name":"运维工具",
           "url":"http://api.my.com.cn/weui/"
       }]
 }
 '''
        url = 'https://qyapi.weixin.qq.com/cgi-bin/menu/create?access_token=%s&agentid=%s' % (token, self.agentid)
        req = urllib2.Request(url, post)
        response = urllib2.urlopen(req)
        return response
