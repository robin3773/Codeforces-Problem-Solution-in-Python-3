test_case = int(input())

for _ in range(test_case):
    l = list(map(int, input().split()))

    if l[0] != l[-1]:
        print(l[0], l[-1])
    else:
        print(l[1], l[-1])
