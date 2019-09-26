#coding:utf-8
import time
#协程方式实现多任务(使用yield)
def work1():
    num = 1
    while num < 10:
        print("this is work1")
        num += 1
        yield
        time.sleep(0.5)

def work2():
    num = 1
    while num<10:
        print("this is work2")
        num += 1
        yield
        time.sleep(0.5)

def main():
    w1 = work1()
    w2 = work2()
    num = 1
    while num < 10:
        next(w1)
        next(w2)
        num += 1

if __name__ == '__main__':
    main()
