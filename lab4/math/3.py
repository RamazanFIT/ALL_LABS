import math 

def S(n, a):
    return (n * pow(a, 2)) / (4 * math.tan(math.pi / n))

list_1 = list(map(int, input().split()))

print(S(*list_1))