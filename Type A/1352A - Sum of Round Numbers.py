test_case = int(input())

while test_case:
    n = list(input())
    length = len(n) - 1
    summnads = [int(a) * 10**(length - idx) for (idx, a) in enumerate(n) if a != '0']
    print(len(summnads))
    print(*summnads)

    test_case -= 1
