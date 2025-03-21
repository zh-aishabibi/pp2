import os 

print(os.getcwd) # Prints the current working directory

#os.mkdir("new_folder") # Creates "new_folder" in the current directory

#os.makedirs("getready/childfolder/grandchild") #This is like creating folders manually inside each other.
#os.makedirs("parent/child/grandchild") 

print(os.listdir())

files = [f for f in os.listdir() if os.path.isfile(f)]
for x in files:
    print(x)
