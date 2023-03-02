import re  
str_1 = str(input("Plz, enter a string: "))

pattern = r"a(b*)"

if re.search(pattern, str_1):
    print("Yes")
else:
    print("No")


