import os

name = input("enter name of file: ")

# with open (name , "x") as file:
#     file.write("created")

if os.path.exists(name):
    print("it was created")

if os.path.exists(name):
    os.remove(name) 
    print ("sadly or badly it was removed")
else:
    print("it does not exist already!")