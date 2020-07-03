year = int(input()) + 1

while True:
    y = str(year)
    if len(set(y)) == len(y):
        print(year)
        break
    year += 1
