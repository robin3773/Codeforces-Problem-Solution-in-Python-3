test_case = int(input())

for _ in range(test_case):
    a, b, c, d, k = map(int, input().split())

    no_pen = (a + c - 1) // c
    no_pencil = (b + d - 1) // d

    print(*([no_pen, no_pencil],  [-1])[no_pencil + no_pen > k])

