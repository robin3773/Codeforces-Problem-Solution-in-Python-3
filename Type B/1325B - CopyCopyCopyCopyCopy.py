test_case = int(input())

for _ in range(test_case):
    n = int(input())
    a = set(map(int, input().split()))

    print(len(a))
