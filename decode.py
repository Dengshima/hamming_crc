#!/usr/bin/env python
# coding=utf-8

def decode_fun(hamming,data):
    n=len(hamming)
    r=0
    #获取校验位数
    while 1:
        if 2**r-1>=n:
            break
        else:
            r+=1

    pos=0
    for i in range(0,r):
        #print("第%d校验位：" %(i+1))
        tmp=0
        j=2**i
        over=0
        while 1:
            if (j>n) or (over==1):
                if tmp==1:
                    pos+=2**i
                    #print(pos)
                break
            else:
                for k in range(0,2**i):
                    if j+k>n:
                        over=1
                        break
                    else:
                        tmp=tmp^int(hamming[j+k-1])
                        #print(hamming[j+k-1])
                j+=2**(i+1)
    k=n-r
    for i in range(0,k):
        data.append(0)
    j=0
    for i in range(0,n):
        if i&(i+1)!=0:
            if (i+1)==pos:
                data[j]=str(int(not int(hamming[i])))
            else:
                data[j]=hamming[i]
            j+=1
    return pos

def decode_main():
    hamming=input("请输入海明码：")
    data=[]
    p=decode_fun(hamming,data)
    if p==0:
        print("编码正确")
    else:
        print ("第%d位出错" %(p))
    print("原数据为：")
    print(''.join([str(x) for x in data]))

if __name__=='__main__':
    decode_main()
