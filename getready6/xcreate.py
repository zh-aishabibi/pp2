import os 

name = "example.txt"

if os.path.exists(name):
    print ("choose dif name")

else:
    with open(name, "x") as f:
        print("new file!") #can use write only if file doesn't exist 
    
    with open(name, "a") as f:
        f.write("cannot be blank. It is boring!")