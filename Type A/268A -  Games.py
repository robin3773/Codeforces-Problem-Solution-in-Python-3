# n = int(input())
# teams = []
# for i in range(n):
#     teams.append([int(x) for x in input().split()])
#
# count = 0
# for i in range(n):
#     for j in range(n):
#         if teams[i][1] == teams[j][0]:
#             count += 1
#
# print(count)

# Alternate solution
n = int(input())
a, b = zip(*(input().split() for _ in ' ' * n))
print(a, b)
print(sum(a.count(x) for x in b))
