#coding:utf-8
import gevent

def work1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)


# g1 = gevent.spawn(work1,5)
# g2 = gevent.spawn(work1,5)
# g3 = gevent.spawn(work1,5)
# g1.join()
# g2.join()
# g3.join()
#结果如下：可以看到结果是依次运行不是交替运行：
# <Greenlet at 0x10dd96050: work1(5)> 0
# <Greenlet at 0x10dd96050: work1(5)> 1
# <Greenlet at 0x10dd96050: work1(5)> 2
# <Greenlet at 0x10dd96050: work1(5)> 3
# <Greenlet at 0x10dd96050: work1(5)> 4
# <Greenlet at 0x10dd96170: work1(5)> 0
# <Greenlet at 0x10dd96170: work1(5)> 1
# <Greenlet at 0x10dd96170: work1(5)> 2
# <Greenlet at 0x10dd96170: work1(5)> 3
# <Greenlet at 0x10dd96170: work1(5)> 4
# <Greenlet at 0x10dd96290: work1(5)> 0
# <Greenlet at 0x10dd96290: work1(5)> 1
# <Greenlet at 0x10dd96290: work1(5)> 2
# <Greenlet at 0x10dd96290: work1(5)> 3
# <Greenlet at 0x10dd96290: work1(5)> 4

#gevent切换运行
def work(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #用来模拟一个耗时操作，是gevent中的sleep
        gevent.sleep(1)

# g1 = gevent.spawn(work,5)
# g2 = gevent.spawn(work,5)
# g3 = gevent.spawn(work,5)
# g1.join()
# g2.join()
# g3.join()
#执行结果如下：
# <Greenlet at 0x111139050: work(5)> 0
# <Greenlet at 0x111139170: work(5)> 0
# <Greenlet at 0x111139290: work(5)> 0
# <Greenlet at 0x111139050: work(5)> 1
# <Greenlet at 0x111139170: work(5)> 1
# <Greenlet at 0x111139290: work(5)> 1
# <Greenlet at 0x111139050: work(5)> 2
# <Greenlet at 0x111139170: work(5)> 2
# <Greenlet at 0x111139290: work(5)> 2
#给程序打补丁：
from gevent import monkey
import gevent
import random
import time

#有耗时操作时需要
monkey.patch_all() #将程序中用到的耗时操作代码，换成gevent中自己实现的模块
def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name,i)
        time.sleep(random.random())

gevent.joinall([
                gevent.spawn(coroutine_work,"work1"),
                gevent.spawn(coroutine_work,"work2")
                ])
#运行结果
# work1 0
# work2 0
# work2 1
# work2 2
# work1 1
# work1 2
# work2 3
# work1 3
# work1 4
# work2 4
# work1 5
# work2 5
# work2 6
# work1 6
# work2 7
# work1 7
# work1 8
# work2 8
# work1 9
# work2 9



