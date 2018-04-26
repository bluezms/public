#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/4/25 17:09
# @Author  : zms
# @Site    : 
# @File    : SendEmail.py
# @Software: PyCharm Community Edition

import time
from email.mime.text import MIMEText
import smtplib


class SendEmail(object):
    def __init__(self):
        self.port = 25
        self.fromemail = 'test@test.com'
        self.emailpasswd = '******'

    def sendemail(self, subject, msg, fromemail=None, emailpasswd=None, toemail=None):
        '''实现发送邮件功能函数'''
        if fromemail == None | emailpasswd == None:
            _user = self.fromemail
            _pwd = self.emailpasswd
        else:
            _user = fromemail
            _pwd = emailpasswd
        _to = toemail
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S')

        msg = MIMEText(msg)
        msg["Subject"] = subject
        msg["From"] = _user
        msg["To"] = _to

        try:
            # s = smtplib.SMTP_SSL('****.****.cn', 25)
            s = smtplib.SMTP('****.****.cn', self.port)
            s.login(_user, _pwd)
            s.sendmail(_user, _to, msg.as_string())
            s.quit()
            print "[%s]INFO:%s Email send Success!" % (nowtime, _to)
        except smtplib.SMTPException, e:
            print "[%s]ERROR:%s Email send Falied,%s" % ((nowtime, e), _to)


if __name__ == '__main__':
    email = SendEmail()
    email.sendemail('test', 'test', 'test@test.com', '******', 'test@test.com')
