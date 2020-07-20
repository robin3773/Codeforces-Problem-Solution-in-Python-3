n = int(input())
a = list(map(int, input().split()))

result = [0, 0, 0]
string = ['chest', 'biceps', 'back']
j = 0
for i in range(n):
    result[j % 3] += a[i]
    j += 1

print(string[result.index(max(result))])

# Alternate Solution
index = max([0, 1, 2], key=(lambda x: sum(a[i::3])))
print(string[index])
