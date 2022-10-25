# -*- UTF-8 -*-

# 求无序整数列表的中位数。如列表元素为偶数个，则取列表升序排列时中间两数中数值
# 较小的元素为中位数。
import random

def assignment22(list_input):
    #例子 list_input=[2,3,5,1,4,6]
    #       output=3  取list_input升序排序后[1,2,3,4,5,6]中间两个元素的较小元素
    L = sorted(list_input)
    size = len(list_input)
    if size%2==1:
        result = L[(size+1)//2]
    else:
        result = L[(size//2)]
    return result
    
if __name__ == '__main__':
    n = random.randint(20,40)
    list_input= [random.randint(1,100) for x in range(n)]

    result=assignment22(list_input)
    print(result)