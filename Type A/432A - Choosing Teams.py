n, k = map(int, input().split())
y = map(int, input().split())

number_of_team = sum([(y + k) <= 5 for y in y]) // 3
print(number_of_team)
