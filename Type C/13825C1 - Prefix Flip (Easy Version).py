def convert(arr, prefix):
    for p in prefix:
        # print(arr[:p])
        arr[:p] = reversed([str(1 - int(i) * 1) for i in arr[:p]])
        # print(arr)

    return arr


# print(convert(list('01011'), [5, 1, 5, 4, 1, 4, 3, 1, 3, 1]))

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    a = list(input())
    b = list(input())

    if a == b:
        print(0)
        continue

    result = []
    for i in range(n - 1, 0, -1):
        if a[i] != b[i]:
            result += ([i + 1, 1, i + 1])

    if a[0] != b[0]:
        result += [1]

    print(*result)
    print(convert(a, result) == b)
