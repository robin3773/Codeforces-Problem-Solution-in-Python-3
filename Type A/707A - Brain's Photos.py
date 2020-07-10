n, m = map(int, input().split())

color = []

for i in range(n):
    color += input().split()

argument = set(color) & set('CYM')
print('#Color' if argument else '#Black&White')