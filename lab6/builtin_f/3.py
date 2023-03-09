def pol(str_1):
    return str_1.lower() == str_1[::-1].lower()
    
str_1 = str(input())
print(pol(str_1))