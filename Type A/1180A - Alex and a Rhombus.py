n = int(input())
"""
There are 1, 3, 5, ....., 2n-3 cells in each row below 
and above the largest row and there are 2n-1 cells in 
the largest row. 
n - 1: number of row above the largest row
"""
print(2 * n ** 2 - 2 * n + 1)    # 2*(n-1)**2 + (2n-1)
