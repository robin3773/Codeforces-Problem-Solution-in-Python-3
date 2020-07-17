n = int(input())
a = list(map(int, input().split()))

maximum = sub_len = length = 0

for i in a:
    sub_len = sub_len + 1 if i > maximum else 1
    maximum = i
    length = max(length, sub_len)

print(length)
