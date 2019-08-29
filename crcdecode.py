#!/usr/bin/env python
# coding=utf-8

def crc_decode(data,rule):
    r=len(rule)-1     #添加0个数为多项式位数-1
    data1=data
    #print(data1)
    n=len(data1)
    rule1=bin(int(rule,2)<<(len(data1)-len(rule)))[2:]
    #print(rule1)
    strtmp=''
    for i in range(0,n):
        strtmp=strtmp+'0'
    while 1:
        strtmp=bin(int(data1,2)^int(rule1,2))[2:]
        #print(strtmp)
        data1=strtmp
        if len(strtmp)<r+1:
            strtmp=strtmp.zfill(r)
            break
        else:
            rule1=bin(int(rule,2)<<(len(strtmp)-r-1))[2:]
            #print(rule1)
    return strtmp

def crc_main():
    data=input("请输入数据crc编码串：")
    #rule=input("请输入数字代表生成多项式规则：例如8代表crc-8")
    rule=input("请输入生成多项式：")
    strtmp=crc_decode(data,rule)
    if int(strtmp,2)==0:
        print("编码正确")
    else:
        print("编码错误，丢弃重传")

if __name__=='__main__':
    crc_main()
