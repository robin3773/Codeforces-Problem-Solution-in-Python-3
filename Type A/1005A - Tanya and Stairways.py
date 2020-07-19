n = int(input())
a = list(map(int, input().split()))

l = [x for (x, y) in zip(a, a[1:] + [1]) if y == 1]
print(len(l))
print(*l)