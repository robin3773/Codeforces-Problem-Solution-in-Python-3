test_case = int(input())

while test_case:
    n = int(input())
    print((1 << (n//2+1)) - 2)

    test_case -= 1

