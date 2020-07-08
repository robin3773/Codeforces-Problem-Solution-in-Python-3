p = set(input().strip('{}').split(', '))
print(len(p) - 1 if '' in p else len(p))

# alternate solution
print(len(set(input()+', '))-4)