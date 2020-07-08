import sys

inputs = list()
for i in range(0, 5):
    inputs.append(int(input()))

d = count = inputs[-1]
inputs = inputs[:-1]

if 1 in inputs:
    print(d)
    sys.exit()

for i in range(1, d + 1):
    if i % inputs[0] and i % inputs[1] and i % inputs[2] and i % inputs[3]:
        count -= 1


print(count)
