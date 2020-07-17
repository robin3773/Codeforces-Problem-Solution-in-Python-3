def abc(x, y, z):
    for a in [x, y, z]:
        for b in [x, y, z]:
            for c in [x, y, z]:
                if max(a, b) == x and max(a, c) == y and max(b, c) == z:
                    return a, b, c


test_case = int(input())

for _ in range(test_case):
    x, y, z = map(int, input().split())
    result = abc(x, y, z)

    if result is None:
        print('NO')
    else:
        print('YES')
        print(*result)
