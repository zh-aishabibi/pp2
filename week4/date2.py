import datetime
a = datetime.datetime.today()
b = datetime.timedelta(days=1) 

print (f"today is: {a} and yesterday was: {a-b} and tomorrow will be: {a+b}")