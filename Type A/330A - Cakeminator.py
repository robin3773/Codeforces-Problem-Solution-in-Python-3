r, c = map(int, input().split())
cake_row = [input() for i in range(r)]

free_row = len([1 for i in cake_row if 'S' not in i])
free_col = len([1 for i in zip(*cake_row) if 'S' not in i])

print(free_col * (r-free_row) + free_row*c)

