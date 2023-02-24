import datetime 

date_1 = datetime.datetime(*list(map(int, input("Year, month, day, hour, minutes, seconds: ").split())))
date_2 = datetime.datetime(*list(map(int, input("Year, month, day, hour, minutes, seconds: ").split())))
difference = abs(date_2 - date_1)

print("difference Between 2 dates in seconds: ", difference.days * 24 * 60 * 60 + difference.seconds , "seconds")