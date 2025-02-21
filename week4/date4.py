import datetime 
a = datetime.datetime.now()
b = input("Enter a date (YYYY-MM-DD h:m:s): ")
c = datetime.datetime.strptime(b, "%Y-%m-%d %H:%M:%S")

d = a - c
print(d.total_seconds())