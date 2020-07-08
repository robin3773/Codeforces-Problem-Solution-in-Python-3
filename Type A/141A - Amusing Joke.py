guest = input()
host = input()
jumble = sorted(input())

print('YES' if sorted(host+guest) == jumble else 'NO')

