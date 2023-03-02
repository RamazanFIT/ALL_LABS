def div_by_3_4(k: int):
    for i in range(12, k+1, 12):
        yield i

in_1 = int(input())

it = div_by_3_4(in_1)
mass = []
for i in it:
    mass.append(i)

if(len(mass) == 0):
    print("No elements")
else:
    print(*mass)