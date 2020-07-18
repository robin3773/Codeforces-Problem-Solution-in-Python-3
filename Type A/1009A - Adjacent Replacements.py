n = int(input())
a = list(map(int, input().split()))

a = [i + i%2 - 1 for i in a]
print(*a)
