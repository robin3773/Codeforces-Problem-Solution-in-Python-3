# My Solution
word = input()
n_upper = sum(1 for c in word if c.isupper())
n_lower = len(word) - n_upper

print(word.upper() if n_upper > n_lower else word.lower())

# Alternate Solution
word = input()
print([word.lower(), word.upper()][sum(map(str.isupper, word)) > len(word) / 2])
