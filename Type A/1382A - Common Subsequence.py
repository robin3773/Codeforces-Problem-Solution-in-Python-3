test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    temp_a = [i for i in a if i in b]
    temp_b = [i for i in b if i in a]

    # print(temp_a, temp_b)
    if temp_b == [] or temp_a == []:
        print('NO')
        continue

    print('YES')
    print(1, temp_a[0])