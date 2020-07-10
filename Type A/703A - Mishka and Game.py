n = int(input())

win_m = win_c = 0
result = ['Mishka', 'Chris', 'Friendship is magic!^^']
while n:
    m, c = map(int, input().split())
    win_m += m >= c
    win_c += m <= c

    n -= 1

print(result[2] if win_c == win_m else result[win_m < win_c])