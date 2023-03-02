import re   

pattern = r"([a-z]+)_([a-z]+)"

s = str(input("enter a word: "))

if re.search(pattern, s):
    print('yes')
else:
    print('no')