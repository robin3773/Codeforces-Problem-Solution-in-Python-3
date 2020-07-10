test_case = int(input())

while test_case:
    a, b = sorted(map(int, input().split()))
    print(max(2*a, b)**2)

    test_case -= 1
