x = int(input())

category = [4, 1, 3, 2]

new_category = category[x % 4]
if new_category == 4:
    print(1, 'A')
elif new_category == 1:
    print(0, 'A')
elif new_category == 3:
    print(1, 'B')
else:
    print(2, 'A')
    
