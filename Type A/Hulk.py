# My Solution

n = int(input())
string = str()
out_string = ['I hate ', 'I love ']
conjunction = ['that', '']

i = 0

while n:
    string += out_string[i] + conjunction[n == 1]
    n -= 1
    i = (i + 1) % 2

print(string, end='it')

# Alternate Solution/ Smart Solution

print(*(['I hate', 'I love'] * 50)[:int(input())], sep=' that ', end=' it')
