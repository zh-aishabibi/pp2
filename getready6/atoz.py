import string
import os

for letter in string.ascii_uppercase:
   filename = f"{letter}.txt"

   if not os.path.exists(filename):
      with open (filename, "w") as f:
         f.write(f'{letter} file created')

