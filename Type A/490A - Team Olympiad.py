n = int(input())
t = list(map(int, input().split()))

s = sorted(enumerate(t, 1), key=(lambda x: x[1]))
ones = [(a, b) for (a, b) in s if b == 1]
twos =[(a, b) for (a, b) in s if b == 2]
threes = [(a, b) for (a, b) in s if b == 3]
count = [len(ones), len(twos), len(threes)]

print(min(count))
for i in range(min(count)):
    print(ones[i][0], twos[i][0], threes[i][0])


