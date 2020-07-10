test_case = int(input())

while test_case:
    n = int(input())
    s = sorted(map(int, input().split()))

    print(min([abs(a - b) for (a, b) in zip(s, s[1:])]))

    test_case -= 1


