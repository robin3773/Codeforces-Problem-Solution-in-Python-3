test_case = int(input())

for _ in range(test_case):
    n = int(input())
    a = list(map(int, input().split()))

    maximum, max_idx = max(a), a.index(max(a))
    result = [0] * (n + 1)

    # maximum_string = ''.join([chr(i) for i in range(97, 97 + maximum)])
    # result[max_idx], result[max_idx + 1] = [maximum_string, maximum_string]

    i = j = 0
    k = 25
    while 0 in result:
        if a[i]:
            result[j] = ''.join([chr(97 + i % 26) for i in range(a[i])])
        else:
            result[j] = ''.join(chr(97 + k % 26))
            k -= 1

        if j != max_idx:
            i += 1

        j += 1

    print(*result, sep='\n')
