k2, k3, k5, k6 = map(int, input().split())

no_256 = min(k2, k5, k6)
no_32 = max(0, min(k2-no_256, k3))

print(256*no_256 + 32 * no_32)