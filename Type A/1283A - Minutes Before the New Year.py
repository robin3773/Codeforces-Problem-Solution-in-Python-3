test_case = int(input())

for _ in range(test_case):
    h, m = map(int, input().split())

    print(24 * 60 - h * 60 - m)