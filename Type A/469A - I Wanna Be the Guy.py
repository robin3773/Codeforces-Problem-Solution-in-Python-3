n = int(input())
p, *X = list(map(int, input().split()))
q, *Y = list(map(int, input().split()))

result = set(X + Y)
argument = len(result) >= n

print("I become the guy." if argument else "Oh, my keyboard!")

# # Alternate Solution
# a = input
# print("IO hb,e cmoym ek etyhbeo agrudy!."[int(a()) > len(set(a().split()[1:] + a().split()[1:]))::2])
