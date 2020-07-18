test_case = int(input())

for _ in range(test_case):
    n = int(input())
    a = list(map(int, input().split()))

    zeros = a.count(0)
    summation = sum(a)

    print(zeros + (summation + zeros == 0))
