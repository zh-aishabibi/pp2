l = input().split()
filename = input("file: ")

f = f"{filename}.txt"

def listtofile(l, f ):
    with open(f, 'w') as file:
        for x in l:
            file.write(f"{x}\n")

print(listtofile(l,f))                       
with open(f,'r') as fil:
    print(fil.read())