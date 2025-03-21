import datetime

time1 = datetime.datetime.now() #First datetime is the module, second is the class.
time2 = datetime.timedelta(days=5)
yest = datetime.timedelta(days=1)

a = input("enter in that way (YYYY-MM-DD HH:MM:SS)")
maked = datetime.datetime.strptime(a,"%Y-%m-%d %H:%M:%S" )#Converts a formatted date string into a datetime object.
print(maked)

b = time1.replace(second=0, microsecond=0 ,hour=0, minute=0)
print (b)

c = time1.strftime('%Y-%B-%d-%A %H') #we can construct the pattern by ourselves Converts a datetime object into a formatted string.
print(c)

print (f"today is {time1.strftime("%A")} ")

print(time1-time2)
print (f"yest was {(time1-yest).date()} tomor is {time1+yest}")