#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/4/25 17:06
# @Author  : zms
# @Site    : 
# @File    : WeChat.py
# @Software: PyCharm Community Edition

# !/usr/bin/env python
# coding:utf-8
# file wechat.py

import time
import requests
import json

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class WeChat:
    def __init__(self):
        self.CORPID = 'wwf93d8138e15e65d6'
        self.CORPSECRET = 'ZW2_CbZck4eVSfevT-qENZpzQXuDhHfBuw0A-Fvr4jI'
        self.AGENTID = '1000002'
        self.TOUSER = "ZhengMingShe"  # 接收者用户名

    def _get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': self.CORPID,
                  'corpsecret': self.CORPSECRET,
                  }
        req = requests.post(url, params=values)
        data = json.loads(req.text)
        # print data
        return data["access_token"]

    def get_access_token(self):
        try:
            with open('./tmp/access_token.conf', 'r') as f:
                t, access_token = f.read().split()
        except:
            with open('./tmp/access_token.conf', 'w') as f:
                access_token = self._get_access_token()
                cur_time = time.time()
                f.write('\t'.join([str(cur_time), access_token]))
                return access_token
        else:
            cur_time = time.time()
            if 0 < cur_time - float(t) < 7260:
                return access_token
            else:
                with open('./access_token.conf', 'w') as f:
                    access_token = self._get_access_token()
                    f.write('\t'.join([str(cur_time), access_token]))
                    return access_token

    def send_data(self, message):
        msg = message.encode('utf-8')
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.get_access_token()
        send_values = {
            "touser": self.TOUSER,
            "msgtype": "text",
            "agentid": self.AGENTID,
            "text": {
                "content": msg
                },
            "safe": "0"
            }
        send_data = '{"msgtype": "text", "safe": "0", "agentid": %s, "touser": "%s", "text": {"content": "%s"}}' % (
            self.AGENTID, self.TOUSER, msg)
        r = requests.post(send_url, send_data)
        # print r.content
        return r.content


if __name__ == '__main__':
    wx = WeChat()
    wx.send_data("6不6")
