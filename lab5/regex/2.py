import re

pattern = r"a(b{2}|b{3})$"

str_1 = str(input("plz, enter a string: "))

if re.search(pattern, str_1):
    print('yes')
else:
    print('no')
