n = int(input())
sentence = input().lower()
if n < 26:
    print('NO')
    exit()

print('Yes' if len(set(sentence)) >= 26 else 'NO')
