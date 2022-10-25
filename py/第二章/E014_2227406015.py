money = 0
for month in range(1,6):
    money=(100+money)*(1+0.005)
benefit = money-500
print("五个月后,存款金额为{0:.2f}元,收益率为{1:.2%}".format(money,benefit/500))