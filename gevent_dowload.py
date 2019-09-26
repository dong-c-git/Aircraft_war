#coding:utf-8
from gevent import monkey
import gevent
import urllib.request
#有耗时操作时候需要
monkey.patch_all()

def my_download(url):
    print("GET:%s"%url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print("%d bytes received from %s."%(len(data),url))

gevent.joinall([
    gevent.spawn(my_download,"http://www.baidu.com"),
    gevent.spawn(my_download,"http://www.itcast.cn/"),
    gevent.spawn(my_download,"http://www.itheima.com/"),
                ])

#执行结果：（结果中收到数据顺序和执行时顺序无关，体现在异步上）
# GET:http://www.baidu.com
# GET:http://www.itcast.cn/
# GET:http://www.itheima.com/
# 138849 bytes received from http://www.itcast.cn/.
# 154143 bytes received from http://www.baidu.com.
# 226026 bytes received from http://www.itheima.com/.

#修改为多视屏下载器，添加写入方法即可：
def my_download(url,file_name):
    print("GET:%s"%url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print("%d bytes received from %s."%(len(data),url))

    with open(file_name,"wb") as fp:
        fp.write(data)

    print("%s视屏已经下载了"%file_name)

gevent.joinall([
    gevent.spawn(my_download,"http://www.baidu.com","1.mp4"),
    gevent.spawn(my_download,"http://www.itcast.cn/","4.mp4"),
    gevent.spawn(my_download,"http://www.itheima.com/","3.mp4"),
                ])