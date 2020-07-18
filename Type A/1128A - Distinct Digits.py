l, r = map(int, input().split())

all_distinct = (lambda s: len(set(s)) == len(s))
for i in range(l, r + 1):
    if all_distinct(str(i)):
        print(i)
        exit()

print(-1)
