#coding:utf-8

class Mylist(object):
    def __init__(self):
        self.container = []
    def add(self,item):
        self.container.append(item)
    def __iter__(self):
        """返回一个迭代器"""
        #迭代器必须有的一个方法，暂时忽略如何构造一个迭代器对象
        pass
# mylist = Mylist()
# #判断是否是迭代器
# from collections.abc import Iterable
# ret = isinstance(mylist,Iterable)
# print(ret)

class MyList(object):
    """自定义的一个可迭代对象"""
    def __init__(self):
        self.items = []
        #self.current = 0

    def add(self, val):
        self.items.append(val)

    # def __next__(self):   #自己类中实现迭代器
    #     if self.current < len(self.items):
    #         item = self.items[self.current]
    #         self.current += 1
    #         return item
    #     else:
    #         raise StopIteration

    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator
        #return self #改写到自己类中实现迭代器


class MyIterator(object):
    """自定义的供上面可迭代对象使用的一个迭代器"""
    def __init__(self, mylist):
        self.mylist = mylist
        # current用来记录当前访问到的位置
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)
    for num in mylist:
        print(num)

#迭代器是实现斐波那契数列：
class Feibonaqi(object):
    def __init__(self,n):
        self.n = n
        self.current = 0
        self.num1 = 0
        self.num2 = 1

    def __next__(self):
        if self.current < self.n:
            num = self.num1
            self.num1,self.num2 = self.num2,self.num1+self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        return self

# if __name__ == '__main__':
#     fib = Feibonaqi(10)
#     for num in fib:
#         print(num,end=" ")
#     #除了for循环可以接收可迭代对象，list和tuple也可以接收可迭代对象
#     li = list(Feibonaqi(15))
#     print(li)
#     tp = tuple(Feibonaqi(6))
#     print(tp)