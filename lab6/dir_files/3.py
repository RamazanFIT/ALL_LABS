import os
path = str(input("Path: "))

print("Yes" if os.path.exists(path) else "NO")
# Just name
print(os.path.basename(path)) if os.path.exists(path) else print("No")
# Just a path to this file
print(os.path.dirname(path) if os.path.exists(path) else print("No"))