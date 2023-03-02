def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2 

a, b = tuple(map(int, input().split()))

print(*squares(a, b))