test_case = int(input())

while test_case:
    n = int(input())
    if (n / 2) % 2:
        print('NO')
    else:
        even_series = [i for i in range(2, n + 1, 2)]
        odd_series = [i for i in range(1, n - 2, 2)] + [n//2 * 3 - 1]

        print('YES')
        print(*(even_series + odd_series))

    test_case -= 1
