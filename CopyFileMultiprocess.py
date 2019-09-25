#coding:utf-8
from multiprocessing import Manager,Pool
import os,time,random

def copy_file(queue,file_name,source_folder_name,dest_folder_name):
    """copy文件到指定的路径"""
    f_read = open(source_folder_name+'/'+file_name,"rb")
    f_write = open(dest_folder_name+"/"+file_name,"wb")
    while True:
        time.sleep(random.random())
        content = f_read.read(1024)
        if content:
            f_write.write(content)
        else:
            break
    f_read.close()
    f_write.close()
    #发送已经拷贝完毕的文件名字：
    queue.put(file_name)


def main():
    #1、获取需要复制的文件夹：
    source_folder_name = input("请输入要复制文件夹名字：")
    #2、整理目标文件夹：
    dest_folder_name = source_folder_name+"[副本]"
    #3、创建目标文件夹
    try:
        os.mkdir(dest_folder_name)
    except:
        pass
    #4、获取需要复制文件夹下所有文件
    source_file_list = os.listdir(source_folder_name)
    #5、创建进程池添加任务:
    queue = Manager().Queue()
    pool = Pool(3)
    for file_name in source_file_list:
        pool.apply_async(copy_file,args=(queue,file_name,source_folder_name,dest_folder_name))

    #主进程显示：
    pool.close()
    all_file_num = len(source_file_list)
    while True:
        file_name = queue.get()
        if file_name in source_file_list:
            source_file_list.remove(file_name)
        copy_rate = (all_file_num-len(source_file_list))*100/all_file_num
        print("\r%.2f....(%s)"%(copy_rate,file_name)+" "*50,end="")
        if copy_rate >=100:
            break
    print()


if __name__ == '__main__':
    main()
