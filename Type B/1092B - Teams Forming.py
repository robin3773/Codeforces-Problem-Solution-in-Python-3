n = int(input())
a = sorted(map(int, input().split()))

print(sum([a[i+1] - a[i] for i in range(0, n, 2)]))

