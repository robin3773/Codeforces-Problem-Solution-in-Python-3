n = int(input())
a = list(enumerate(map(int, input().split()), 1))
a.sort(key=lambda x: x[1])

for i in range(n//2):
    print(a[i][0], a[n-1-i][0])
