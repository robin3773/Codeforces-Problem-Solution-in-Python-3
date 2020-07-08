test_case = int(input())
while test_case:
    a, b = map(int, input().split())
    print(0 if not a % b else b - a % b)
    test_case -= 1
