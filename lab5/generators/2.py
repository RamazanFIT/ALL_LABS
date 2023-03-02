def even(k: int):
    for i in range(0, k+1, 2):
        yield i


in_1 = int(input())

it = even(in_1)
cnt = 0 
for i in it:
    print(i, end = "")
    if cnt == in_1 // 2:
        continue 
    print(", ", end = '')
    cnt += 1


