# n = int(input())
# events = list(map(int, input().split()))
#
# i = count = police = 0
#
# for i in range(n):
#     if events[i] > 0:
#         if police > 0:
#             police += events[i]
#         else:
#             police = events[i]
#     else:
#         police -= 1
#
#     if police < 0:
#         count += 1
#
# print(count)


# Alternate solution
n = input()
events = list(map(int, input().split()))
crime = 0

for i in events[::-1]:
    crime = min(0, crime + i)
print(-crime)
