test_case = int(input())

while test_case:
    n, m = map(int, input().split())

    print(min(2, n - 1) * m)

    test_case -= 1
