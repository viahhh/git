# -*- UTF-8 -*-

#随机生成一个 10 以内整数平方的列表，要求从大到小排序

import random
def assignment24():
    # step1: 生成一个随机整数，表示列表元素个数
    n=random.randint(1,10)
    
    # step2: 根据n生成一个10以内的随机整数平方的列表
    x = random.randint(1,10)
    lst=list(x ** 2 for x in range(n))
    
    # step3: 对lst进行降序排序
    lst=lst[::-1]    
    result=lst
    
    return result
    
    
if __name__ == '__main__':
    result=assignment24()
    print(result)