test_case = int(input())

while test_case:
    b = input()
    print(b[:-1:2] + b[-1])

    test_case -= 1
