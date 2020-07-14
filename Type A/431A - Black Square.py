a = input().split()

s = input()
print(sum([int(a[int(i)-1]) for i in s]))

