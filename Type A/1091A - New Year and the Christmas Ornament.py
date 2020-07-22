y, b, r = map(int, input().split())

for i in range(r, -1, -1):
    for j in range(b, -1, -1):
        for k in range(y, -1, -1):
            if i - j == 1 and j - k == 1:
                print(i + j + k)
                exit()