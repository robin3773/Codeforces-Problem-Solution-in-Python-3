n, k = map(int, input().split())
a = list(map(int, input().split()))

no_distinct_element = len(set(a))
# print(no_distinct_element, set(a))

if no_distinct_element < k:
    print('NO')
else:
    print('YES')
    print(*[a.index(i)+1 for i in list(set(a))[:k]])