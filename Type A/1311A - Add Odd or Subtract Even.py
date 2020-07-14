test_case = int(input())

for _ in range(test_case):
    a, b = map(int, input().split())

    if a == b:
        print(0)

    elif b > a:
        if (b - a) % 2:
            print(1)
        else:
            print(2)
    else:
        if (a - b) % 2:
            print(2)
        else:
            print(1)

# Alternate Solution
for _ in [0] * int(input()):
    a, b = map(int, input().split())
    b -= a
    print(b and ((b < 0) & b | (b > 0) & ~b) + 1)
