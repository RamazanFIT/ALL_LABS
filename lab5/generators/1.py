def gen_square(k):
    for i in range(1, k+1):
        yield i ** 2 

in_1 = int(input())

print(*gen_square(in_1))