n, t = map(int, input().split())
sequence = input()

for i in range(t):
    sequence = sequence.replace('BG', 'GB')

print(sequence)
