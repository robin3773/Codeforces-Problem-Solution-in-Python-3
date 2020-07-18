n, c = map(int, input().split())
t = list(map(int, input().split()))

count = 1
for i in range(n - 1):
    if t[i + 1] - t[i] <= c:
        count += 1
    else:
        count = 1


print(count)
