test_case = int(input())

for _ in range(test_case):
    n = int(input())
    a = list(map(int, input().split()))

    all_even = sum([1 for i in a if i % 2 == 0]) == n
    all_odd = sum([1 for i in a if i % 2 == 1]) == n

    if all_even or (all_odd and n % 2 == 0):
        print('NO')
        continue

    print('YES')
