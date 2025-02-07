def seven():
    n = input()
    mylist = [int(x) for x in n.split() ]
    for i in range(len(mylist)-2):
        if mylist[i]== 0 and mylist[i+1]== 0 and mylist[i+2]== 7:
            return True 
        
    return False 

print (seven())