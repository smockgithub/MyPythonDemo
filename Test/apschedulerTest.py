#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.jianshu.com/p/7beb242b5b34

from apscheduler.schedulers.blocking import BlockingScheduler  #pip install apscheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time
import logging
import sys

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename='log1.log',
#                     filemode='a')

def job1():
    print(sys._getframe().f_code.co_name)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'hello world 1')
    time.sleep(6)
    # a=1/0 # 异常不会影响任务正常结束

def job2():
    
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'hello world 2')
    time.sleep(4)

scheduler = BlockingScheduler() #在主线程执行，会阻塞主线程。
scheduler.add_job(job1, 'interval', seconds=5)
scheduler.add_job(job2, 'interval', seconds=5)

# scheduler._logger=logging #日志
scheduler.start() #阻塞 等待 不会执行后面了

scheduler = BackgroundScheduler() #不会阻塞主线程，所以在start之后要保障主线程不会关闭
scheduler.add_job(job1, 'interval', seconds=5) #间隔3秒钟执行一次
scheduler.add_job(job2, 'interval', seconds=5) #间隔3秒钟执行一次
# scheduler.start()

input("any key to exit")
