import tkinter
root = tkinter.Tk()
root.geometry("600x400")
root.configure(background="black")

List = [
    "10.新一期作文礼包派发！",
    "9.并桌之事，有何新？",
    "8.近期北京沙尘暴，注意防范",
    "7.某国核污水决定排放",
    "6.圆柱与圆锥制作困难，同学们勇于尝试",
    "5.英语即将开始阶段性测试，学霸学神：不怕的",
    "4.信息技术二组全员出动！",
    "3.回忆友谊，欢乐与泪水",
    "2.星座展示趣事！",
    "1.《四人组》第一季完本，敬请期待第二季",
    "近期六12班热点震撼来袭"
    ]
Num = 0

def renew():
    global listb, List, Num
    listb.insert(0, List[Num])
    Num = Num+1listb = tkinter.Listbox(root,width=60,height=20,bg="black",fg="yellow"  )
listb.pack()

button1 = tkinter.Button(root,text="黑客更新", command=renew)
button1.pack()     
root.mainloop()
