prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

n, m = map(int, input().split())
index = int([(a, b) for (a, b) in enumerate(prime) if b == n][0][0])
# print(index)
print('NO' if (index == 14 or m != prime[index+1]) else 'YES')
