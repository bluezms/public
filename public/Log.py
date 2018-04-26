#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/4/25 17:05
# @Author  : zms
# @Site    : 
# @File    : Log.py
# @Software: PyCharm Community Edition

import time
import logging
import os
from logging.handlers import RotatingFileHandler

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = project_dir + r"\log\\"


class Log(logging.Logger):
    def __init__(self, logname):
        # super(MyLogger, self).__init__(filename)
        filename = log_path + logname + '.log'
        logging.Logger.__init__(self, filename)

        # 设置日志格式
        fmtHandler = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)s][%(levelname)s] %(message)s')

        # 终端log输出流设置
        try:
            consoleHd = logging.StreamHandler()
            consoleHd.setLevel(logging.ERROR)
            consoleHd.setFormatter(fmtHandler)
            self.addHandler(consoleHd)
        except Exception as reason:
            self.error("%s" % reason)

            # 设置log文件
        try:
            os.makedirs(os.path.dirname(filename))
        except Exception as reason:
            pass
        try:
            # 设置回滚日志,每个日志最大10M,最多备份5个日志
            fileHd = logging.handlers.RotatingFileHandler(
                filename, maxBytes=10 * 1024 * 1024, backupCount=5)
            # fileHd = logging.FileHandler(filename)
            fileHd.setLevel(logging.INFO)
            fileHd.setFormatter(fmtHandler)
            self.addHandler(fileHd)
        except Exception as reason:
            self.error("%s" % reason)

        return



if __name__ == '__main__':
    test1 = Log('test1')
    test2 = Log('test2')
    while True:
        test1.error("test1")
        test2.error("test2")
