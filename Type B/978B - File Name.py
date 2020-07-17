n = int(input())
string = input()

curr_pos = sub_len = 0
length = []
temp = 0

for i in range(n):

    if string[i] == 'x':
        sub_len += 1

    if string[i] != 'x' or i == n - 1:
        length.append(sub_len)
        sub_len = 0

    # print(string[i], sub_len)

print(sum([i-2 for i in length if i > 2]))