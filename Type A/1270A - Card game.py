test_case = int(input())

for _ in range(test_case):
    n, k1, k2 = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print('YES' if n in a else "NO")
