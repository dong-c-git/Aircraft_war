#coding:utf-8
from greenlet import greenlet
import time

def worker1():
    num = 0
    while num < 10:
        print("this is worker 1")
        num += 1
        gr2.switch()
        time.sleep(0.5)

def worker2():
    num = 0
    while num < 10:
        print("this is worker 2")
        num += 1
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(worker1)
gr2 = greenlet(worker2)

#切换到gr1中运行
gr1.switch()

