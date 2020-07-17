test_case = int(input())


for _ in range(test_case):
    x, y, a, b = map(int, input().split())

    print(-1 if (y-x) % (a+b) else (y-x)//(a+b))