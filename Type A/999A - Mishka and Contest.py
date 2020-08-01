n, k = map(int, input().split())
a = list(map(int, input().split()))

index = [i for i in range(n) if a[i] > k]
print(n - (index[-1] - index[0] + 1) if index else n)
