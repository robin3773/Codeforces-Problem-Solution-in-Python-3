test_case = int(input())

for _ in range(test_case):
    n, x, a, b = map(int, input().split())

    print(min(n-1, abs(a-b)+x))
