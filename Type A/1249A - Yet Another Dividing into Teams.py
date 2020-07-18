test_case = int(input())

for _ in range(test_case):
    n = int(input())
    a = sorted(map(int, input().split()))

    argument = 1 in [(a[i + 1] - a[i]) for i in range(n - 1)]

    print(2 if argument else 1)
