a = int(input())

summation = (lambda s: sum([int(i) for i in str(s)]))
while summation(a) % 4:
    a += 1

print(a)