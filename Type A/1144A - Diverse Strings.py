test_case = int(input())

for _ in range(test_case):
    string = (input())
    print('YES' if (ord(max(string)) - ord(min(string)) + 1) == len(string) and len(string) == len(set(string))
          else 'NO')
