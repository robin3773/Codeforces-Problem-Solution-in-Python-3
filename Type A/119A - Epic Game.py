*fixed_number, n = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


i = 0
while n:
    n -= gcd(fixed_number[i % 2], n)
    i += 1

print(0 if i % 2 else 1)
