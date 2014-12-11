#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys

def init():
    pid = os.fork()
    if pid:
        os.waitpid(pid, 0)
        os.system("notify-send '程序运行结束' 'pid:%d %s'" % (pid, sys.argv[0]))
        exit()
