def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


Y, W = map(int, input().split())
numerator = (6 - max(Y, W) + 1)
print('%d/%d' % (numerator // gcd(numerator, 6), 6 // gcd(numerator, 6)))
