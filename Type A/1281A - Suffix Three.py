test_case = int(input())

for _ in range(test_case):
    sentence = input()
    
    if sentence.endswith('po'):
        print('FILIPINO')
    elif sentence.endswith('masu') or sentence.endswith('desu'):
        print('JAPANESE')
    else:
        print('KOREAN')