test_case = int(input())

for _ in range(test_case):
    n = int(input())
    s = input()

    index_8 = s.find('8')
    # print(index_8)
    print('YES' if (n - index_8 >= 11 and index_8 != -1) else 'NO')