# -*- UTF-8 -*-

# 现有列表[35,46,57,13,24,35,99,68,13,79,88,46]，请编写程序将其中重复的元素去除，并
# 按从小到大的顺序排列后输出。

from itertools import count
from os import remove


def assignment30(List):
    # 例子：input:[35,46,57,13,24,35,99,68,13,79,88,46]
    # result:[13, 24, 35, 46, 57, 68, 79, 88, 99]

    #step1: 删除lst中重复元素，使得重复元素只保留一份
    for i in List[:]:
        if List.count(i)>=2:
            List.remove(i)

    #step2: 对temp_lst进行升序排序
    result=sorted(List)

    return result

if __name__ == '__main__':
    lst= [35,46,57,13,24,35,99,68,13,79,88,46]
    result=assignment30(lst)
    print(result)