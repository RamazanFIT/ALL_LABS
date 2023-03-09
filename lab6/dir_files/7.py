import os
print("Copy from ENTER to ENTER")
from_1 = str(input("from link: "))
to_1 = str(input("to link: "))

if os.path.exists(from_1):
    global f1 
    f1 = open(from_1, 'r')

some_inf = f1.readlines()

if os.path.exists(to_1):
    global f2
    f2 = open(to_1, 'w')
f2.writelines(some_inf)
