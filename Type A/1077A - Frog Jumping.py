test_case = int(input())

for _ in range(test_case):
    a, b, k = map(int, input().split())

    print(k//2*(a-b) + (k % 2) * a)