import re   

pattern = r"(^[A-Z])([a-z]+)"

s = str(input("enter a word: "))

if re.search(pattern, s):
    print('yes')
else:
    print('no')

    