#coding:utf-8
import re
#判断变量名是否有效
names = ["name1","_name","2_name","__name__","!name"]

for i in names:
    ret = re.match("[A-Za-z_]+[\w]*",i)
    if ret:
        print("%s 是合法变量名"%ret.group())
    else:
        print("%s 不是合法变量名"%i)

#匹配0-99
ret1 = re.match("[0-9]?[0-9]","0")
print(ret1.group())

#匹配出8-20位的密码
ret2 = re.match("[a-zA-Z0-9_]{6}","1ad12f23s34455ff66")
print(ret2.group())

#匹配出163邮箱地址@符号之前有4-20位
ret3 = re.match("[a-zA-Z0-9]{4,20}@163\.com","hello@163.com")
print(ret3.group())

#匹配数字修正（错误情况08）
# 修正之后的
ret4 = re.match("[1-9]?\d$","08")
if ret4:
    print(ret4.group())
else:
    print("不在0-100之间")
#匹配到100的数字
ret5 = re.match("[1-9]?\d$|100","08")
if ret5:
    print(ret5.group())
else:
    print("不在0-100之间")

#匹配多种格式邮箱（163、126、qq）
ret6 = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret6.group())  # test@163.com

#匹配不是47结尾的手机号
ret7 = re.match("1\d{9}[0-35-68-9]","13100001233")
print(ret7.group())
#提取区号和电话号码
ret8 = re.match("([^-]*)-(\d+)","010-12345678")
print(ret8.group())
print(ret8.group(1),ret8.group(2))
#匹配出<html>hh</html
ret9 = re.match("<[a-zA-Z]*>[a-zA-Z]*</[a-zA-Z]*>","<html>hh</html>")
print(ret9.group())
#匹配出<html><h1>www.itcast.cn</h1></html>
# ret10 = re.match("<(\w)*><(\w)*>.*</\2></\1>","<html><h1>www.itcast.cn</h1></html>")
# print(ret10.group())

ret10 = re.match(r"<(\w*)><(\w*)>.*</\2></\1>","<html><h1>www.itcast.cn</h1></html>")
print(ret10.group())
#使用别名方式
ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
print(ret.group())