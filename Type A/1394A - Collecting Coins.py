test_case = int(input())

for _ in range(test_case):
    a, b, c, n = map(int, input().split())

    B = (a - 2 * b + c + n) // 3
    A = b - a + B
    C = b - c + B

    print('YES' if (A + B + C == n and A >= 0 and B >= 0 and C >= 0) else 'NO')
