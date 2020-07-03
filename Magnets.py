n = int(input())
t = n
magnets = list()
while t:
    magnets.append(input())
    t -= 1

group = 0
slider = magnets[0]

for i in range(1, n):
    # print(slider, magnets[i])/
    if slider != magnets[i]:
        # print(slider, magnets[i])
        slider = magnets[i]
        group += 1

print(group + 1)

# Alternate Solution
import sys

ms = sys.stdin.readlines()[1:]
print(sum([1 for (a, b) in zip(ms, ms[1:]) if a != b]) + 1)
