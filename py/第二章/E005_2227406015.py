x,y,z=map(int,input("请分别输入三个整数x y z:").split())
if x<=y<=z:
    print(x,y,z)
elif x<=z<=y:
    print(x,z,y)
elif y<=x<=z:
    print(y,x,z)
elif y<=z<=x:
    print(y,z,x)
elif z<=x<=y:
    print(z,x,y)
else:
    print(z,y,x)