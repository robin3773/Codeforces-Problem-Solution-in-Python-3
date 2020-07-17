test_case = int(input())

for _ in range(test_case):
    a = list(map(int, input().split()))
    print(sum(a)//2)
