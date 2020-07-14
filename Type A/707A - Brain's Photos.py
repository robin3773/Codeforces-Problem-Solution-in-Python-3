import sys
n, m = map(int, input().split())

argument = set(sys.stdin.readline()) & set('CYM')
print('#Color' if argument else '#Black&White')