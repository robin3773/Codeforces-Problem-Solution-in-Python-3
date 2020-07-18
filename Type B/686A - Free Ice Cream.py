n, x = map(int, input().split())

ice_cream = x
distress_child = 0
for _ in range(n):
    sign, amount = input().split()

    if sign == '+':
        ice_cream += int(amount)
    elif sign == '-' and ice_cream >= int(amount):
        ice_cream -= int(amount)
    elif sign == '-' and ice_cream<int(amount):
        distress_child += 1

print(ice_cream, distress_child)
