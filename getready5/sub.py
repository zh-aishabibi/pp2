import re

txt = input("cd: ")

#x = re.sub(r"[\s,\.]" , ":", txt) #we only need [] (square brackets) when we want to match multiple different characters.

#. * + ? ( ) { } [ ] ^ $ | \ needs \ special

x = re.sub(r"([A-Z])", r" \1", txt) #\1 used with groups so dont forget () and r
y = re.sub(r"[A-Z]", " ", txt)
print(x)
print(y)