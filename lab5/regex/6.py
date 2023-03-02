import re   

txt = str(input("enter a sentences: "))

x = re.sub(' ', ',', txt)
x = re.sub('[.]', ';', x)

print(x)