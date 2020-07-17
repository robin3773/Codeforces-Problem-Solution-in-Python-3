name = input().strip()

code = [1] + [ord(i) - 96 for i in name]

no_moves = 0
for i in range(len(code) - 1):
    no_moves += min(abs(code[i] - code[i+1]), 26 - abs(code[i] - code[i+1]))

print(no_moves)
