test_case = int(input())

for _ in range(test_case):
    n = int(input())
    a = list(map(int, input().split()))

    if sum(a) == n:
        print('First' if n % 2 else 'Second')
        continue

    for i in range(n):
        if a[i] != 1:
            print('Second' if i % 2 else 'First')
            break
