test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())

    print('NO' if m * n > m + n else 'YES')
