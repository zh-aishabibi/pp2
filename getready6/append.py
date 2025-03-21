f = open("getready/v.txt", "a+")

f.write("one more line at the end\n") #from new line
f.writelines(["hello\n", "world!\n"])

f.seek(0) #after adding to the end cursor is in the end as well
print(f.read())

f.close()

# "a" allows only to write, to read we can either reopen the file at "rt" mode or use "a+"

# "a" changes the existinf file but if file doesnt exist it craetes it 

#To write to an existing file, you must add a parameter to the open() function:
#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content
