x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

argument = a >= x and b + a >= x + y and a + b + c >= x + y + z
print('YES' if argument else 'NO')
