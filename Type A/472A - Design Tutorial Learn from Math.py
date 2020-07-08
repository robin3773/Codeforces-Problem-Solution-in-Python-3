n = int(input())
result = [[8, n - 8], [9, n - 9]]
print(*result[n % 2])