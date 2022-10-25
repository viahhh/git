import math
x1,y1=eval(input('请输入第一个向量:'))
x2,y2=eval(input('请输入第二个向量:'))
cosa=abs(x1*x2+y1*y2)/(math.sqrt(x1**2+y1**2)*math.sqrt(x2**2+y2**2))
print(cosa)