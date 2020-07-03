n = int(input())
gift_to = list(map(int, input().split()))
gift_from = gift_to.copy()

for i in range(n):
    gift_from[gift_to[i]-1] = i+1

print(*gift_from)
