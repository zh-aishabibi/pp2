import string 
import os

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"

    if os.path.exists(filename):
        os.remove(filename)