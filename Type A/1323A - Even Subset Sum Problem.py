test_case = int(input())

# for _ in range(test_case):
#     n = int(input())
#     a = list(map(int, input().split()))
#
#     odd_count = sum([1 for i in a if i % 2])
#     even_count = n - odd_count
#
#     if even_count == 0:
#         if odd_count < 2:
#             print(-1)
#         else:
#             print(2)
#             print(1, 2)
#         continue
#
#     print(1)
#     print([i+1 for i in range(n) if a[i] % 2 == 0][0])
#
#

# Alternate solution
for _ in range(test_case):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] % 2 == 0:
        print(1, 1, sep='\n')
    elif n == 1:
        print(-1)
    elif a[1] % 2 == 0:
        print(1, 2, sep='\n')
    else:
        print(2)
        print(1, 2)
