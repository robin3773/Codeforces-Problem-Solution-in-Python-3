cipher = input()
match = ['.', '-.', '--']

for i in range(len(match) - 1, -1, -1):
    cipher = cipher.replace(match[i], str(i))

print(cipher)
