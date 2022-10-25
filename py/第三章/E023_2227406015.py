# -*- UTF-8 -*-

# 已知一个整数列表，判断列表内容是否为回文，即无论正序还是倒序，列表的内容是否相同。

def assignment23(list_input):
    #例子 list_input=[1,2,3,4,3,2,1]
    #       output=True
    list_r = list_input[::-1]
    if list_r == list_input:
        return True
    else:
        return False

    #例子 list_input=[1,2,4,4,3,2,1]
    #       output=False

    
if __name__ == '__main__':
    list_input = [1, 2, 3, 4, 3, 2, 1]
    result=assignment23(list_input)
    print(result)