test_case = int(input())

for _ in range(test_case):
    n = int(input())

    result = [6, 10, 14]

    if n < 31:
        print('NO')
    else:
        if n - 30 in result:
            result[2] = 15
        print('YES')
        print(*[*result, n - sum(result)])
