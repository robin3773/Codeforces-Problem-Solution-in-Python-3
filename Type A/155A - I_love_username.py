number_of_contest = int(input())
points = list(map(int, input().split()))
count = 0


def check(points, point):
    # print(points, point, max(points), min(points))
    if point < min(points) or point > max(points):
        return True
    return False


for i in range(1, number_of_contest):
    if check(points[:i], points[i]):
        count += 1

print(count)


# Alternate Solution
n = int(input())
points = list(map(int, input().split()))

min = max = points[0]
count = 0
for i in range(1, n):
    if points[i] < min:
        min = points[i]
        count += 1
    if points[i] > max:
        max = points[i]
        count += 1

print(count)
