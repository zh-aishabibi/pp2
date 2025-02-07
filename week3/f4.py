def prime(x):
    for i in range (2, int(x**0.5 + 1)):
        if (x%i==0):
            return False
    return True 

def sort(numbers):
    return [num for num in numbers if prime(num)]
    
n = input()
mylist = []

for x in n.split():
    mylist.append(int(x))

print (sort(mylist))