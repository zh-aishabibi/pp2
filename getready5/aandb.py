import re 

txt = input("enter a sentence: ")

pattern = r"a.*b$"
x = re.findall(pattern , txt)
y = re.search(pattern , txt)
z = re.match(pattern, txt)
print(x) #list
if y:
    print(y.span())
    print(y.group()) #string
if z:
    print(z.span())
    print(z.group())

#span returns the start and end indexes of the first occurance
#group gives sequence of first occuranmce , string just rewrites the orig  

#findall = all ; search = first accurance ; match = first element txt[0] only.