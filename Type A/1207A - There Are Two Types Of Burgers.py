test_case = int(input())

for _ in range(test_case):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())

    profit = 0
    bun = b // 2

    if bun < 1:
        print(0)
        continue

    maximum = max(h, c)

    if maximum == c:
        profit = min(bun, f) * c + min(p, max(0, bun-f)) * h
    else:
        profit = min(bun, p) * h + min(f, max(0, bun-p)) * c

    print(profit)
