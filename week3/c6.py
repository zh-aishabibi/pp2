def isprime (x):
    if x < 2 :
        return False
    elif x>=2 :
        for i in range(2, int(x**0.5+1)):
            if x%i == 0:
                return False 
    return True 

a = input("list: ")
mylist = [int(x) for x in a.split() ]

print (list(filter(lambda x: isprime(x) , mylist))) 

        
    
 
