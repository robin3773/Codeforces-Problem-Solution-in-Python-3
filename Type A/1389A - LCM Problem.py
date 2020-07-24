test_case = int(input())

for _ in range(test_case):
    l, r = map(int, input().split())

    print(*[l, 2 * l] if 2 * l <= r else [-1]*2)
