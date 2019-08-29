#!/usr/bin/env python
# coding=utf-8
from crcencode import crc_encode
from crcdecode import crc_decode
from tkinter import *
root=Tk()
root.title("CRC编码程序")
toptitle = Label(root, text="CRC编码过程", bg="white", font=("Arial", 12), height=2)
toptitle.pack(side=TOP)

def tk_encode():
    data=var.get()
    rule_str=rule.get()
    flag=1
    if len(data)==0 or len(rule_str)==0:
        text.insert(END,'输入错误\n')
    else:
        for i in range(0,len(data)):
            if data[i]!='0' and data[i]!='1':
                flag=0
        for i in range(0,len(rule_str)):
            if rule_str[i]!='0' and rule_str[i]!='1':
                flag=0
        if data[0]!='1':
            flag=0
        if rule_str[0]!='1':
            flag=0
        if flag==0:
            text.insert(END,'输入错误，请重新输入\n')
        else:
            encodes=crc_encode(data,rule_str)
            text.insert(END,data+'的CRC编码为：\n')
            text.insert(END,''.join([str(x) for x in encodes]))
            text.insert(END,'\n')

def tk_decode():
    data2=var2.get()
    rule_str2=rule2.get()
    flag=1        #用来检验输入数据正误

    if len(data2)==0 or len(rule_str2)==0:
        text2.insert(END,'请重新输入：\n')
    else:
        for i in range(0,len(data2)):
            if data2[i]!='0' and data2[i]!='1':
                flag=0
        for i in range(0,len(rule_str2)):
            if rule_str2[i]!='0' and rule_str2[i]!='1':
                flag=0
        if rule_str2[0]!='1':
            flag=0
        if data2[0]!='1' or data2[len(data2)-1]!='1':
            flag=0
        if flag==0:
            text2.insert(END,'输入有误，请重新输入\n')
        else:
            strtmp=crc_decode(data2,rule_str2)
            if int(strtmp,2)==0:
                text2.insert(END,'编码正确\n')
                #print("编码正确")
            else:
                text2.insert(END,'编码错误，丢弃重传\n')
                #print("编码错误，丢弃重传")

#编码部分的图形界面
var = StringVar()
top_1=Label(root, text="请输入数据码", bg="white", font=("Arial", 8),  height=2)
top_1.pack()
e = Entry(root, textvariable = var)
e.pack()
rule = StringVar()
top_2=Label(root, text="请输入生成多项式", bg="white", font=("Arial", 8), height=2)
top_2.pack()

rule_e = Entry(root, textvariable = rule)
rule_e.pack()
Button(root, text="输入完成", command = tk_encode).pack()
text=Text(height=4)
text.pack()
   
#纠错部分的图形界面
toptitle2 = Label(root, text="CRC编码纠错", bg="white", font=("Arial", 12), height=2)
toptitle2.pack(side=TOP)
var2 = StringVar()
bot_1=Label(root, text="请输入CRC码", bg="white", font=("Arial", 8), height=2)
bot_1.pack()
e2 = Entry(root, textvariable = var2)
e2.pack()
rule2=StringVar()
bot_2=Label(root, text="请输入生成多项式", bg="white", font=("Arial", 8), height=2)
bot_2.pack()
rule_e2 = Entry(root, textvariable = rule2)
rule_e2.pack()
Button(root, text="输入完成", command = tk_decode).pack()
text2=Text(height=4)
text2.pack()

Button(root, text="退出", command = exit).pack()
root.mainloop()

