string = input()

count = 0
length = len(string)
for i in range(length):
    if string[i] == 'Q':
        for j in range(i, length):
            if string[j] == 'A':
                for k in range(j, length):
                    if string[k] == 'Q':
                        count += 1

print(count)

# Alternate solution
count = 0
for i in range(length):
    if string[i] == 'A':
        count += string[:i].count('Q') * string[i:].count('Q')


print(count)
