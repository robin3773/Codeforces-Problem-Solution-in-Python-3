n = int(input())
A = {}

for i in range(n):
    for j in range(n):
        if not (i and j):
            A[str(i) + str(j)] = 1
        else:
            A[str(i) + str(j)] = A[str(i - 1) + str(j)] + A[str(i) + str(j - 1)]

print(A[str(n-1) + str(n-1)])
