import re   



def snake_to_camel(str_1):
    str_1 = list(str_1.split('_'))
    str_2 = str(str_1[0])
    for i in range(1, len(str_1)):
        str_2 += (str_1[i][0]).upper()
        str_2 += str_1[i][1:]
    return str_2
# snake ---> camel 

s = str(input("enter a string: "))

ans = snake_to_camel(s)

print(ans)


