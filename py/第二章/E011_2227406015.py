from cmath import pi


h,r=eval(input("请输入高(cm)和半径(cm),用逗号隔开:"))
v = pi*(r**2)*h
num = int(20000//v)
yushu = 20000%v
if yushu != 0:
    num = num+1
print("需要%d桶"%num)