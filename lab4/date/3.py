import datetime 

time_now = datetime.datetime.now()

time_now = time_now.replace(microsecond = 0)

print(time_now)

