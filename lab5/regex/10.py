import re   

# camel -------> snake
def camel_to_snake(str_1):
    pattern = r'[A-Z][a-z]*'
    first_str = str(re.findall(r'[a-z]+', str_1)[0])
    list_1 = re.findall(pattern, str_1)
    list_2 = [x.lower() for x in list_1]
    list_2.insert(0, first_str)
    return '_'.join(list_2)
s = str(input("enter a str: "))

ans = camel_to_snake(s)
print(ans)
