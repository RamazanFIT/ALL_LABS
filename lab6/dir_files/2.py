import os 
path = str(input("Path: "))
# C:\Users\Akken\Desktop\labs\lab6\dir_files\1.py
print("File exists?: ", "Yes" if os.access(path, os.F_OK) else "NO")


print("File readable?: ", "Yes" if os.access(path, os.R_OK) else "NO")


print("File writable?: ", "Yes" if os.access(path, os.W_OK) else "NO")


print("File executable?: ", "Yes" if os.access(path, os.X_OK) else "NO")