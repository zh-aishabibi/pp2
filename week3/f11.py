def pol(str):
    str2 = str[::-1]
    if str == str2:
        return True 
    return False 

s = input()
print(pol(s))