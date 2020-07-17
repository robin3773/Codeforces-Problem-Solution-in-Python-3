n = int(input())

card_numbers = list(map(int, input().split()))

result = [0, 0]

i = 0
while card_numbers:
    # print(card_numbers[0], card_numbers[-1])
    result[i % 2] += max(card_numbers[0], card_numbers[-1])
    card_numbers.remove(max(card_numbers[0], card_numbers[-1]))
    # print(card_numbers)
    i += 1


print(*result)
