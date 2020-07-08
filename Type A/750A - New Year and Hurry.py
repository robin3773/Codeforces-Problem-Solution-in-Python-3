n, k = map(int, input().split())
remaining_time = 240 - k
# print(remaining_time)
for i in range(n, 0, -1):
    # print(i)
    if (5 * i * (i + 1)) / 2 <= remaining_time:
        print(i)
        exit()

print(0)
