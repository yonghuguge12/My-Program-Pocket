import time
print("欢迎来到董老师在线投诉中心")
print("投诉电话：12345")
print("投诉受理内容：\n 1.作业问题 \n 2.学科问题 \n 3.学生辅导 \n 4.成绩问题 \n 5.其他")
a = input("请输入问题序号：")
if a == "1":
    input("请输入详细内容：")
    sleep(1)
    print("投诉成功！")
if a == "2":
    input("请输入详细内容：")
    sleep(1)
    print("投诉成功！")
if a == "3":
    input("请输入详细内容：")
    sleep(1)
    print("投诉成功！")
if a == "4":
    input("请输入详细内容：")
    sleep(1)
    print("投诉成功！")
if a == "5":
    input("请输入详细内容：")
    sleep(1)
    print("投诉成功！")
else:
    print("没有搜寻到投诉受理内容")
