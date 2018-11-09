#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from lxml import etree
import sys
from WXBizMsgCrypt import WXBizMsgCrypt
import xml.etree.cElementTree as ET
import os
import sys
import time

sys.path.append("..")
import system.ping as ping
import system.ss_vpn as ssvpn
import system.tcping as tcping
import system.cpt_deploy as cpt_deploy
import system.jenkins as jks
import system.jiradb as jiradb
from globalvar import MyGlobals


class QYWXapi(object):
    def __init__(self):
        self.logger = web.ctx.environ['wsgilog.logger']
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, '../templates')
        self.render = web.template.render(self.templates_root)
        self.sToken = 'your_token'
        self.sEncodingAESKey = 'your_key'
        self.sCorpID = 'your_ID'
        # 获取url验证时微信发送的相关参数
        self.wxcpt = WXBizMsgCrypt(self.sToken, self.sEncodingAESKey, self.sCorpID)
        self.data = web.input()
        self.sVerifyMsgSig = self.data.msg_signature
        self.sVerifyTimeStamp = self.data.timestamp
        self.sVerifyNonce = self.data.nonce

    def SendMsg(self, toUser, fromUser, content):
        sReplyMsg = str(self.render.reply_text(toUser, fromUser, int(time.time()), content))
        sTimeStamp = str(time.time())
        sNonce = self.sVerifyNonce
        # 加密发送消息
        ret, sEncryptMsg = self.wxcpt.EncryptMsg(sReplyMsg, sNonce, sTimeStamp)
        if (ret != 0):
            print "ERR: EncryptMsg ret: " + ret
            sys.exit(1)
        return sEncryptMsg

    def GET(self):
        sVerifyEchoStr = self.data.echostr
        ret, sEchoStr = self.wxcpt.VerifyURL(self.sVerifyMsgSig, self.sVerifyTimeStamp, self.sVerifyNonce,
                                             sVerifyEchoStr)
        if (ret != 0):
            print "ERR: VerifyURL ret:" + str(ret)
            sys.exit(1)
        return sEchoStr

    def POST(self):
        sReqData = web.data()
        # 解密
        ret, sMsg = self.wxcpt.DecryptMsg(sReqData, self.sVerifyMsgSig, self.sVerifyTimeStamp, self.sVerifyNonce)
        if (ret != 0):
            print "ERR: VerifyURL ret:" + str(ret)
            sys.exit(1)
        # 解析xml
        xml = etree.fromstring(sMsg)
        msgType = xml.find("MsgType").text
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text
        agentID = xml.find("AgentID").text
        accessip = web.ctx['ip']
        # 接收消息或事件
        if msgType == 'text':
            content = xml.find("Content").text
            contentlog = "qxwx:%s:%s:%s" % (accessip, fromUser, content)
            self.logger.info(contentlog)  # 记录日志文件
            content = 'DEVOPS'
            sEncryptMsg = self.SendMsg(toUser, fromUser, content)
            return sEncryptMsg
        elif msgType == 'event':
            event = xml.find("Event").text
            eventKey = xml.find("EventKey").text
            if event == 'click' and eventKey == 'e3_deploy':
                content = '【E3部署】任务已发起，请稍后！'
                sEncryptMsg = self.SendMsg(toUser, fromUser, content)
                jks.deploy_e3()
                return sEncryptMsg
            elif event == 'click' and eventKey == 'scm_deploy':
                content = '【SCM部署】任务已发起，请稍后！'
                sEncryptMsg = self.SendMsg(toUser, fromUser, content)
                return sEncryptMsg
            elif event == 'click' and eventKey == 'cpt_deploy':
                rs = cpt_deploy.deploy()
                if rs == '0':
                    content = '【CPT部署】任务已发起，请稍后！'
                    sEncryptMsg = self.SendMsg(toUser, fromUser, content)
                    jks.deploy_cpt()
                    return sEncryptMsg
                else:
                    content = '【CPT部署】任务异常，请排查！'
                    sEncryptMsg = self.SendMsg(toUser, fromUser, content)
                    return sEncryptMsg
            elif event == 'click' and eventKey == 'ss_restart':
                content = 'ShadowSocks重启完毕！'
                ssvpn.restart_ss()
                sEncryptMsg = self.SendMsg(toUser, fromUser, content)
                return sEncryptMsg
            elif event == 'click' and eventkey == 'boom':
                content = '数据已全部摧毁，跑路吧！'
                sEncryptMsg = self.SendMsg(toUser, fromUser, content)
                return sEncryptMsg
            elif event == 'view' and eventKey == 'http://api.my.com.cn/jira':
                MyGlobals.fromuser = ""
                MyGlobals.fromuser = fromUser
