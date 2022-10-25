lst=[]
for i in range(2,501):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        lst.append(i)
count=0
for n in lst:
    print(n,end=" ")
    count += 1
    if count%5==0:
        print('')