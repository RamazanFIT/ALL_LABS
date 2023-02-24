import datetime 

now = datetime.datetime.now()

yesterday = now - datetime.timedelta(days = 1)
tomorrow = now + datetime.timedelta(days = 1)

print("Now:", now, now.strftime('%A'), sep="  ")
print("Yesterday:", yesterday, yesterday.strftime('%A'), sep="  ")
print("Tomorrow:", tomorrow, tomorrow.strftime('%A'), sep="  ")