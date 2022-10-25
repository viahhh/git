import time
times = int(time.time()) #获取当前世界时间
hours = times // 3600 +8 #转化成小时（中国）
days = hours // 24
hours = hours - days * 24
print("从1970年1月1日零点(中国)到现在过去了",days,"天",hours,"小时")