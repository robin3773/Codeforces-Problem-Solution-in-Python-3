n, h = map(int, input().split())
a = list(map(int, input().split()))

print(sum([(i > h) + 1 for i in a]))
