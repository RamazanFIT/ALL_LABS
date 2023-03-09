from functools import reduce as red
list_1 = list(map(int, input("input a list: ").split()))

def mult(list):
    return red(lambda x, y: x * y, list)

print(mult(list_1))




