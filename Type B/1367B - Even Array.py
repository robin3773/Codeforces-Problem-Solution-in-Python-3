test_case = int(input())

while test_case:
    n = int(input())
    a = list(map(int, input().split()))

    odd = []
    even = []

    for i in range(n):
        if i % 2 != a[i] % 2:
            odd.append(i) if a[i] % 2 else even.append(i)

    print(-1 if (len(odd) != len(even)) else len(odd))

    test_case -= 1

# Alternate Solution
for s in [*open(0)][2::2]:
    a = [int(x) % 2 for x in s.split()]
    print((sum(i % 2 ^ x for i, x in enumerate(a)) // 2, -1)[sum(a) != len(a) // 2])
