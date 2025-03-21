with open("getready/torewrite.txt", "w+") as f:
    f.write("I deleted the content\n")
    f.writelines(["now it has\n", "new lines\n"])
    f.seek(0)
    print(f.read())

#1️⃣ Deletes all existing content in the file (if it already exists).
#2️⃣ Creates a new file if it does not exist.

