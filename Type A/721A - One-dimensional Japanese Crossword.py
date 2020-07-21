n = int(input())
code = input().split('W')
result = [len(c) for c in code if c != '']

print(len(result))
print(*result)
