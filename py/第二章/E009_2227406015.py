import random
num = random.randint(100,999)
gw = num%10
sw = num%100//10
bw = num//100
renum = gw*100+sw*10+bw
print("%d互换后为%d"%(num,renum))