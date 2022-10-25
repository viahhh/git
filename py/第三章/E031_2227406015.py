# -*- UTF-8 -*-

# 编写程序让用户输入两个字符串（一定是小写字母组成），判断两个字符串是否同构。
# 如果有两个字符串，其中一个字符串的字符重新排列后，能变成另一个字符串，那么称
# 为同构。

def assignment31(stringA,stringB):
    # 例子1：输入 ： stringA：“hellow”, stringB:"llehow"
    #       输出:True

    # 例子1：输入 ： stringA：“world”, stringB:"wolrd"
    #       输出:False

    # 提示：可以将两个字符串按照同一种规则进行调整，然后比较调整后的两个字符串是否相等，
    # 如果相等就是同构，否则就不是同构
    lst1=list(stringA)
    lst2=list(stringB)
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    stringA="hellow"
    stringB="llehow"
    result=assignment31(stringA,stringB)
    print(result)