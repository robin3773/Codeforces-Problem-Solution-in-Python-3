n, m = map(int, input().split())
s = input().split()
t = input().split()

test_case = int(input())

for _ in range(test_case):
    y = int(input())

    print(s[(y % n)-1] + t[(y % m) -1])
