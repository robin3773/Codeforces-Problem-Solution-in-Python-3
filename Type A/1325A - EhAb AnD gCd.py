# test_case = int(input())
#
# for _ in range(test_case):
#     x = int(input())
#     print(1, x - 1)
#
# # Bonus Problem


def factors(n):
    factor_list = ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return sorted([item for sub_list in factor_list for item in sub_list])


x = int(input())
gcd = list(factors(x))
print(gcd)

k1k2 = [x//g - 1 for g in gcd]
print(k1k2)

factor = ([factors(k) for k in k1k2])
print(factor)

k1 = [item for f in factor for item in f[:len(f)//2]]
print(set(k1))
k2 = [item for f in factor for item in f[len(f)//2:]]
print(set(k2))
