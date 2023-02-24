import math 

list_1 = list(map(int, input().split()))

def S(a, b):
    return a * b

print(S(*list_1))