test_case = int(input())

for _ in range(test_case):
    *a, n = map(int, input().split())
    a.sort()
    
    i = 0
    while a[0] <= n and a[1] <= n:
        a[i % 2] += a[(i + 1) % 2]
        i += 1

    print(i)
