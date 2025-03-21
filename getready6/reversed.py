a = input("jhp ;   ")

b = "".join(reversed(a)) #reversed(a) returns an iterator, not a readable string.

if a == b:
    print ("true")
else:
    print("false")