test_case = int(input())

for _ in range(test_case):
    x, y, n = map(int, input().split())

    r = n % x

    # print(r, y, x)

    if r >= y:
        print(n - r + y)
    else:
        print(n - r - x + y)
