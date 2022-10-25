# -*- UTF-8 -*-

# 随机生成一个 20 以内的奇数列表,随机生成一个[0,20]的整数 a， 判断 a 是否在列表中。

import random

def assignment25():
    #例子：将随机列表，随机数，和判断结果均返回
    # step1: 生成两个随机整数n和a，n表示列表元素个数
    n = random.randint(1,20)
    a = random.randint(0,21)
    # step2: 根据n生成一个20以内的随机奇数列表
    lst = [i for i in range(n) if i%2==1]
    
    # step3: 判断a是否在lst中    
    result= a in lst
    
    return lst,a,result
    
if __name__ == '__main__':
    lst,a,result=assignment25()
    print(result)