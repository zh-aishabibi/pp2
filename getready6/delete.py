import os 

name = "example.txt"
#to delete a folder we use os.rmdir("name of folder") empty
# if not empty import shutil and use shutil.rmtree

if os.path.exists(name):
    os.remove(name)
    print ("sadly or badly it was removed")
else:
    print("it does not exist already!")