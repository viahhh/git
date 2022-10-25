import random
lst=[]
L=[]
for i in range(16):
    x = random.randint(1,10)
    lst.append(x)
for j in range(4):
    L.append(lst[4*j:4*j+4])
l=L[:]
for a in range(4):
    l[a]=[L[0][a],L[1][a],L[2][a],L[3][a]]


for n in L:
    print(n)
print('的转置矩阵是：')
for n in l:
    print(n)


