import re
text = input("Enter a string: ")

pattern = r'[a-z]*[A-Z][a-z]*'

print(' '.join(re.findall(pattern, text)))

