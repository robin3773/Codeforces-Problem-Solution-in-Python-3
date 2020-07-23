test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    print(min(sum(a), m))
