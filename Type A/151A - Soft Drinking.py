n, k, l, c, d, p, nl, np = map(int, input().split())

total_drink = k * l
total_slice = c * d

print(min([total_drink//(n*nl), total_slice//(1*n), p//(n * np)]))
