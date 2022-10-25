x1,y1=map(float,input("请输入A的坐标x1,y1(用','隔开):").split(","))
x2,y2=map(float,input("请输入B的坐标x2,y2(用','隔开):").split(","))
d = ((x1-x2)**2+(y1-y2)**2)**(1/2)
print(d)