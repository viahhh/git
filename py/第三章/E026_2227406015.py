# -*- UTF-8 -*-

# 现有一个列表[1,3,4,6,6,7,8,8,10,21,22,22]，编写程序，直接操作列表，使得列表不存在
# 重复元素，且元素均小于 10。

from os import remove


def assignment26(lst):
    # 功能：对给定的列表lst，使得列表中不存在重复元素，也就是删除重复元素，只保留一份
    # 例子：input:[1,3,4,6,6,7,8,8,10,21,22,22]
    # result:[1,3,4,6,7,8,10,21,22]
    for i in lst[::]:
        if lst.count(i)>=2:
            lst.remove(i)
    for i in lst[::]:
        if i >= 10:
            lst.remove(i)
    result=lst
    return result
    
if __name__ == '__main__':
    lst=[1,3,4,6,6,7,8,8,10,21,22,22]
    result=assignment26(lst)
    print(result)