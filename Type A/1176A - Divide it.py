test_case = int(input())

for _ in range(test_case):
    n = int(input())

    i = 0
    while n > 1:
        # n = (n // 2) * (not (n % 2)) + ((2 * n) // 3) * (not (n % 3)) + ((4 * n) // 5) * (not (n % 5))
        if n % 2 == 0:
            n = n // 2
        elif n % 3 == 0:
            n = (2 * n) // 3
        elif n % 5 == 0:
            n = (4 * n) // 5
        else:
            i = -1
            break

        i += 1
        # print(n)

    print(i)
