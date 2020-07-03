number_1 = (input())
length = len(number_1)
number_1 = int(number_1, 2)
number_2 = int(input(), 2)
result = bin(number_1 ^ number_2)[2:]
print('0' * (length - len(result)) + result)

# Alternate Solution
i = input
print(''.join('01'[a != b] for a, b in zip(i(), i())))
