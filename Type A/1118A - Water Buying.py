test_case = int(input())

for _ in range(test_case):
    n, a, b = map(int, input().split())

    print((n // 2) * min(2 * a, b) + (n % 2) * a)
