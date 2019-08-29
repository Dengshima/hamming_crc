#!/usr/bin/env python
# coding=utf-8
from encode import encode_fun
from decode import decode_fun
from tkinter import *
root=Tk()
root.title("海明编码程序")
toptitle = Label(root, text="海明编码过程", bg="white", font=("Arial", 12), height=2)
toptitle.pack(side=TOP)

def tk_encode():
    data=var.get()
    flag=1
    if len(data)==0:
        text.insert(END,'输入错误\n')
    else:
        for i in range(0,len(data)):
            if data[i]!='0' and data[i]!='1':
                flag=0
                
        if flag==0:
            text.insert(END,'输入错误\n')
        else:
            hamming=[]
            encode_fun(data,hamming)
            text.insert(END,data+'的海明编码为：\n')
            text.insert(END,''.join([str(x) for x in hamming]))
            text.insert(END,'\n')

def tk_decode():
    hamming=var2.get()
    flag=1
    if len(hamming)==0:
        text2.insert(END,'输入错误\n')
    else:
        for i in range(0,len(hamming)):
            if hamming[i]!='0' and hamming[i]!='1':
                flag=0

        if flag==0:
            text2.insert(END,'输入错误\n')
        else:
            data=[]
            p=decode_fun(hamming,data)
            if p==0:
                text2.insert(END,'编码正确\n')
            else:
                text2.insert(END,"第%d位出错\n" %(p))
                text2.insert(END,"原数据为：")
                text2.insert(END,''.join([str(x) for x in data]))
                text2.insert(END,'\n')

#编码部分的图形界面
var = StringVar()
e = Entry(root, textvariable = var)
e.pack()
Button(root, text="输入完成", command = tk_encode).pack()
text=Text()
text.pack()
   
#纠错部分的图形界面
toptitle2 = Label(root, text="海明译码纠错过程", bg="white", font=("Arial", 12), height=2)
toptitle2.pack(side=TOP)
var2 = StringVar()
e2 = Entry(root, textvariable = var2)
e2.pack()
Button(root, text="输入完成", command = tk_decode).pack()
text2=Text()
text2.pack()

Button(root, text="退出", command = exit).pack()
root.mainloop()

