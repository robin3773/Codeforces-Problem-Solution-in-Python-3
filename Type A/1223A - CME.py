test_case = int(input())

for _ in range(test_case):
    n = int(input())

    print(2 if n == 2 else (n&1))
