test_case = int(input())

for _ in range(test_case):
    n = int(input())
    price = list(map(int, input().split()))
    print(abs(-sum(price)//n))
    # print(sum(price) // n if sum(price) % n == 0 else (sum(price) // n) + 1)
