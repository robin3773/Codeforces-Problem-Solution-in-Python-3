n = input()
current_state = input()
required_state = input()

no_moves = 0
for i in range(int(n)):
    current_digit = current_state[i]
    required_digit = required_state[i]

    digit = list(map(int, [current_digit, required_digit]))
    minimum = min(digit)
    maximum = max(digit)

    no_moves += min(abs(minimum - maximum), abs(10 + minimum - maximum))

print(no_moves)
