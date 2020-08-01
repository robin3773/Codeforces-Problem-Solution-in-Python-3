n = input()
a = list(map(int, input().split()))

for x in set(a):
    [a.remove(x) for _ in range(a.count(x) - 1)]

print(len(a))
print(*a)
