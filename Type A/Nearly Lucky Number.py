# My solution

n = input()

number_of_digit = n.count('4') + n.count('7')

if number_of_digit == 4 or number_of_digit == 7:
    print('YES')
else:
    print('NO')


# Alternate solution

print("NYOE S"[sum(i in '47' for i in input()) in (4, 7)::2].strip())
