n = int(input())

print(*[1, 1, n-2] if n % 3 == 0 else [1, 2, n - 3])
