#The split() function returns a list where the string has been split at each match:
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 2)   #split("to split in this" , when to stop)
print(x)

#The sub() function replaces the matches with the text of your choice:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)  # space will be relaced with 9
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) #replace first 2 occurances 
print(x)