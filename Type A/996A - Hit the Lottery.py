n = int(input())

number_of_bills = 0
if n >= 100:
    number_of_bills += n // 100
    n = n % 100
if n >= 20:
    number_of_bills += n // 20
    n = n % 20
if n >= 10:
    number_of_bills += n // 10
    n = n % 10
if n >= 5:
    number_of_bills += n // 5
    n = n % 5

number_of_bills += n

print(number_of_bills)

