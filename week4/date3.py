import datetime 
a = datetime.datetime.now()
b = a.replace(microsecond=0)
c = a.strftime('%Y-%m-%d %H')
print (f"date without microsecond is: {b} and  without seconds and minutes: {c}")

