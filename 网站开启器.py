# My-Program-Pocket
import webbrowser
from time import*
print("欢迎来到网址开启器")
sleep(1)
print("输入网址示例（如zh.wikipedia.org，www.baidu.com，不用进行HTTP/HTTPS加密")
print("推荐网站")
print("1.info.cern.ch（世界上第一个网站）")
print("2.www.google.com（世界上访问人数最多的网站）")
print("3.zh.wikipedia.org（世界上最大的知识库）")
a = input("请输入网址：")
webbrowser.open("http://"+a)
