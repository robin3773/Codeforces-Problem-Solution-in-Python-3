test_case = int(input())

while test_case:
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()), reverse=True)

    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]

    print(sum(a))

    test_case -= 1

# Alternate solution
R = lambda: map(int, input().split())
t, = R()
for _ in [0] * t:
    n, k = R()
    print(sum(map(max, sorted(R()), sorted(R())[:-1 - k:-1] + [0] * n)))
