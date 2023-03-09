str_1 = str(input())

def up_case(str_1):
    # str_1 = list(filter(lambda x: True if x >='A' and x <= "Z" else False, str_1))
    # return len(str_1)
    
    cnt = sum(1 for i in str_1 if i.isupper())
    return cnt 

def lower_case(str_1):
    # str_1 = list(filter(lambda x: True if x >='a' and x <= "z" else False, str_1))
    # return len(str_1)

    cnt = sum(1 for i in str_1 if i.islower())
    return cnt 


print("cnt of lower case:", lower_case(str_1))

print("cnt of up case:", up_case(str_1))