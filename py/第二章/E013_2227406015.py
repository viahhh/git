def side(x1,y1,x2,y2):
    d = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return d

x1,y1=map(float,input("请输入点A的坐标x1,y1(用','隔开):").split(","))
x2,y2=map(float,input("请输入点B的坐标x2,y2(用','隔开):").split(","))
x3,y3=map(float,input("请输入点C的坐标x3,y3(用','隔开):").split(","))
side1 = side(x1,y1,x2,y2)
side2 = side(x1,y1,x3,y3)
side3 = side(x2,y2,x3,y3)
s=(side1+side2+side3)/2
area=(s*(s-side1)*(s-side2)*(s-side3))**(1/2)
print("三角形面积是%-7.2f"%s)