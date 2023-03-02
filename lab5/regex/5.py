import re   

pattern = r"a(.*)(b$)"

s = str(input("enter a word: "))

if re.search(pattern, s):
    print('yes')
else:
    print('no')