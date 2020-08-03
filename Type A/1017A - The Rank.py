n = int(input())

result = []
for i in range(n):
    result.append((sum(map(int, input().split()))))

jim_score = result[0]
print(sum([1 for r in result if r > jim_score]) + 1)
