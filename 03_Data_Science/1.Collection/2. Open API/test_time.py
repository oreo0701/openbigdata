import datetime


now = datetime.datetime.now()
base_date=str(now.year)+str(now.month)+str(now.day)
base_time=str(now.hour)+str(now.minute)

print(now)
print(base_date)
print(base_time)


#"%Y %m %d %I %M"