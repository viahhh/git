hh1,mm1,ss1=map(int,input("请输入时间点1,格式为hh:mm:ss").split(":"))
hh2,mm2,ss2=map(int,input("请输入时间点2,格式为hh:mm:ss").split(":"))
t1 = hh1*3600+mm1*60+ss1
t2 = hh2*3600+mm2*60+ss2
if t1 > t2:
    t = t1-t2
else:
    t = t2-t1
print("两者相差%d秒"%t)