import re

pattern = r"ab{2,3}"  # 'a' followed by 2 or 3 'b'

txt = "abbbara loves ababbama abdora hares flamingo"

x = re.findall(pattern, txt)
print(x)
y = re.search(pattern, txt)
print(y)
print(y.string)
print(y.span())
print(y.group())

#span returns the start and end indexes of the first occurance
#group gives sequence of first occuranmce , string just rewrites the orig
