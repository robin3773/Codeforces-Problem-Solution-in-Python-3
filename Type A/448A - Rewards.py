a = sum(map(int, input().split()))
b = sum(map(int, input().split()))
n = int(input())

print('YES' if ((a + 5 - 1) // 5 + (b + 10 - 1) // 10) <= n else 'NO')
