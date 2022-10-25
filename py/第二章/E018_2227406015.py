import datetime
now_time = datetime.datetime.now()
t = 100/80*60
end_time=now_time+datetime.timedelta(minutes=t)
print("到达上海的时间是:",end_time.strftime('%H:%M:%S'))
