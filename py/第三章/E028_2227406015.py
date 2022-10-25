# -*- UTF-8 -*-

# 已知一个整数列表，筛选出该列表中不同的质数，并求出该列表中有多少个质数可以表
# 达为该列表中另外两个质数的和。

import random

def assignment28(lst):
    # 例子：input:lst = [1,2,3,3,4,5,5,5,6,7,8,11,13,12,24,25]
    # result1:[2,3,5,7,11,13] lst中所有不重复的质数
    # result2:[3,5,7,13]  result1中能表示成另外两个元素的和的质数
    lst1=[]
    lst2=[]
    # step1: 找出lst中的所有质数，并且要求在结果中不重复
    for i1 in lst[:]:
        x = 2
        for x in range(2,i1):
            if i1 % x == 0:
                break
        else:
            lst1.append(i1)
    for a in lst1[:]:
        if lst1.count(a)>=2:
            lst1.remove(a)
    result1=lst1
    # step2: 找出result1中能表示成另外两个元素的和的元素
    for i2 in lst[:]:
        for j in lst[:]:
            if (i2-j) in lst:
                lst2.append(i2)
    for a in lst2[:]:
        if lst2.count(a)>=2:
            lst2.remove(a)
    result2=lst2
    return result1,result2
if __name__ == '__main__':
    n = random.randint(20,40)
    lst= [random.randint(1,100) for x in range(n)]

    result=assignment28(lst)
    
    print(result)