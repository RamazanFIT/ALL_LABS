list_1 = tuple(map(int, input().split()))

def trap(h, a, b):
    return h * (a + b) / 2

print(trap(*(list_1)))

