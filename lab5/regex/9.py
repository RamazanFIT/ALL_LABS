import re

s = input("Enter a string: ")

pattern = r'[a-z]*[A-Z][a-z]*'
str_1 = ''

for x in re.findall(pattern, s):
    str_1 += (x + ' ')

print(str_1)
