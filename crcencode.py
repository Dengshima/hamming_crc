#!/usr/bin/env python
# coding=utf-8

def crc_encode(data,rule):
    r=len(rule)-1     #添加0个数为多项式位数-1
    data1=bin(int(data,2)<<r)[2:]
    #print(data1)
    n=len(data1)
    rule1=bin(int(rule,2)<<(n-r-1))[2:]
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
    encodes=data+strtmp
    return encodes


def crc_main():
    data=input("请输入数据字符串：")
    #rule=input("请输入数字代表生成多项式规则：例如8代表crc-8")
    rule=input("请输入生成多项式：")
    encodes=crc_encode(data,rule)
    print(encodes)

if __name__=='__main__':
    crc_main()
