n = int(input())

row = list()
temp = True

for i in range(n):
    row.append(input())
    if 'OO' in row[i] and temp:
        row[i] = row[i].replace('OO', '++', 1)
        temp = False

if temp:
    print('NO')

else:
    print('YES')
    print(*[i for i in row], sep='\n')