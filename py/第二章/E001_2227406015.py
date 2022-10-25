num = int(input("请输入一个三位整数:"))
gw = num % 10
sw = num //10%10
bw = num //100
sum = gw+sw+bw
print("%4d"%sum,end="")