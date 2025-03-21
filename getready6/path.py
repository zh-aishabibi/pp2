import os 
from pathlib import Path

file_path = os.path.abspath("v.txt")
p = Path("v.txt").resolve()

print (file_path)
print (p)