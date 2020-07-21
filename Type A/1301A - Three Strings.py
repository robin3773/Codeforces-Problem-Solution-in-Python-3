test_case = int(input())

for _ in range(test_case):
    a, b, c = [list(input()) for i in range(3)]
    # print(a, b, c)

    for i in range(len(a)):
        if a[i] == c[i]:
            b[i], c[i] = c[i], b[i]
        elif b[i] == c[i]:
            a[i], c[i] = c[i], a[i]
        else:
            a[i], c[i] = c[i], a[i]

    # print(''.join(a), ''.join(b), ''.join(c))
    print('YES' if (a == b) else 'NO')
