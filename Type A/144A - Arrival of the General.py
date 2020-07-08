n = int(input()) - 1
height = list(map(int, input().split()))

min_idx = max([a for (a, b) in enumerate(height) if b == min(height)])
max_idx = min([a for (a, b) in enumerate(height) if b == max(height)])
# print(min_idx, max_idx)

required_time = max_idx + n - min_idx - 1 * int(min_idx < max_idx)
print(required_time)