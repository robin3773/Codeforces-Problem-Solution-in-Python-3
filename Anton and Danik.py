n = int(input())
s = input()

n_anton = s.count('A')
n_danik = n - n_anton

if n_anton > n_danik:
    print('Anton')
elif n_danik > n_anton:
    print('Danik')
else:
    print('Friendship')
