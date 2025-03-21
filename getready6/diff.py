 #Explanation
#1️⃣ "r" and "r+" → Require the file to exist; otherwise, you get a FileNotFoundError.
#2️⃣ "x" → Fails if the file exists (FileExistsError). Use this when you only want to create a new file and never overwrite anything.
#3️⃣ "w" and "w+" → Always create a file if missing and overwrite existing content.
#4️⃣ "a" and "a+" → Always create a file if missing and append to the end instead of deleting anything.