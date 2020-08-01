a, b = map(int, input().split())

result = [0, 0, 0]
for i in range(1, 7):
    if abs(i - a) < abs(i - b):
        result[0] += 1
    elif abs(i - a) > abs(i - b):
        result[-1] += 1
    else:
        result[1] += 1

print(*result)
