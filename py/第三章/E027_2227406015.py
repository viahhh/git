# -*- UTF-8 -*-

# 现有一组列表存放了若干姓名，例如["张三","李四",...,"王五"]。请编写程序，将这些姓名
# 的姓氏单独组成一个列表并输出，假定不存在复姓。

def assignment27(lst):
    # 功能：提前列表元素的开始字符，构成新列表
    # 例子：input:lst = ["张三","李四","王五"]； 提取'张'的方法: lst[0][0],提取'李'的方法：lst[1][0]
    # result:["张","李","王"]
    result = []
    for i in lst:
        j = list(i)[0]
        result.extend(j)
    return result
    
if __name__ == '__main__':
    lst=["张三","李四","王五","钱六","赵七"]
    result=assignment27(lst)

    print(result)