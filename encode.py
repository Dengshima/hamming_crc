#!/usr/bin/env python
# coding=utf-8

def encode_fun(data,hamming):
    k=len(data)
    r=0
    #求校验位数r
    while 1:
        if (2**r-1-r) >=k:
            break
        else:
            r+=1
    n=k+r    #海明码总位数
    for i in range(0,n):
        hamming.append(0)

    tmp=0
    j=0
    #将data插入到hamming中，并且获取data值为1的海明下角标
    for i in range(0,n):
        if ((i+1)&i)!=0:
            #print("datapos",i+1)
            hamming[i]=int(data[j])
            if hamming[i]==1:
                tmp=tmp^(i+1)
                #print("site",i+1)
            j+=1
    
    p=bin(tmp)[2::].zfill(r)
    p=p[::-1]
    #print(p)
    j=0
    for i in range(0,n):
        if (i&(i+1))==0:
            hamming[i]=int(p[j])
            j+=1

def encode_main():
    data=input("请输入数据码：")
    hamming=[]    #用来存放最终的海明码，并初始化数组
   
    encode_fun(data,hamming)
    print("海明编码为：")
    ## 将列表转化成字符串输出,因为其中都是int型，需要先转成str才能用join合并
    print(''.join([str(x) for x in hamming]))

if __name__=='__main__':
    encode_main()
