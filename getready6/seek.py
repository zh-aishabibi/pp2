with open("v.txt", "rb") as f:
    print(f.read(9))

    f.seek(1) #moves cursor to n seek(n) from 0 
    print (f.read(15))

    f.seek(5,1) #seek(n,1) moves n charac forword from the current position rbinary must be
    print(f.read())

    f.seek(0,2) #moves cursor to the end 
    print(f.tell()) #how many characters 

    f.seek(0)
    f.read()
    print(f.tell())

#seek(n, m)  m can be: 0 moves n from the start; 1 moves n from the current position(rb); 2 moves n cursor backword from the end 