# n, m = map(int, input().split())
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if i % 2:
#             print('#', end='')
#         elif (i % 4 == 2 and j == m) or (i % 4 == 0 and j == 1):
#             print('#', end='')
#         else:
#             print('.', end='')
#     print('')

# alternate solution
n, m = map(int, input().split())
for i in range(n):
    print(['#' * m, '.' * (m - 1) + '#', '#' * m, '#' + '.' * (m - 1)][i % 4])
