test_case = int(input())

for _ in range(test_case):
    n = int(input())
    student = input().split('A')[1:]

    # print(student)
    print(max([len(i) for i in student]))
