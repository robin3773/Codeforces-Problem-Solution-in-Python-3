table_card = set(input())
hand_cards = set(input())

print('NYOE S'[bool(table_card & hand_cards)::2])
