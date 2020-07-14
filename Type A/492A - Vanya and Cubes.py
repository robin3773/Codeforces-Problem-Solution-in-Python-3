n = int(input())

i = 1
cube_count = 0
height = 0

while True:
    cube_count += (i * (i + 1))/2
    i += 1
    if cube_count > n:
        break
    height += 1


print(height)
