n = int(input())
cipher = input()

result = ''
i = j = 0
while i+j < n:
    result += cipher[i + j]
    j += i
    i += 1


print(result)
