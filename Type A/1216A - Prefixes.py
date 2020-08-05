n = int(input())
string = list(input())

count = 0
for i in range(0, n, 2):
    if string[i] == string[i + 1]:
        # print(string[i], string[i+1])
        # print(chr(1-ord(string[i]) + 2 * ord('a')))
        count += 1
        string[i] = 'a' if string[i] == 'b' else 'b'


print(count, ''.join(string), sep='\n')
