A, B = map(int, input().split())

fact = 1

for i in range(2, min(A, B) + 1):
    fact *= i

print(fact)