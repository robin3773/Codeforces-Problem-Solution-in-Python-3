a= sorted(map(int, input().split()))

result = (a[-1] == sum(a[:-1])) or (a[0] + a[-1]) == (a[1] + a[-2])

print('YES' if result else 'NO')

