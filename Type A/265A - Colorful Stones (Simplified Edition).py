s = input()
t = input()

i = j = 0
while j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1

print(i + 1)
