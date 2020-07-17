test_case = int(input())

for _ in range(test_case):
    n = int(input())
    p = list(map(int, input().split()))

    for i in range(1, n+1):
        p.remove(i)

    print(*p)