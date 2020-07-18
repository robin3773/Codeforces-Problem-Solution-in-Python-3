n, m = map(int, input().split())

count = 0
for a in range(32):  # sqrt(1000) as 1<=n, m<=100
    for b in range(32):
        if a ** 2 + b - n == 0 == a + b ** 2 - m:
            count += 1

print(count)
