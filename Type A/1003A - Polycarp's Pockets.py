n = int(input())
a = list(map(int, input().split()))

max_pocket = max([a.count(i) for i in a])

print(max_pocket)
