def numbers(k):
    for i in range(k, -1, -1):
        yield i

k = int(input())

p1 = numbers(k)

print(*p1)