import check_rule
import random

def number_extraction(count):
    number_list = [i for i in range(1,46)]
    extraction = 0
    result = []
    while True:
        print('-----------------')
        number = random.sample(number_list, 6)
        number = sorted(number)
        if check_rule.check_number(number):
            print('[Success] Test1 : 적합한 숫자입니다.')
            if check_rule.check_number_and_log(number):
                print('[Success] Test2 : 적합한 숫자입니다.')
                if check_rule.check_number_and_extraction(number, result):
                    print('[Success] Test3 : 적합한 숫자입니다.')
                    print(number)
                    result.append(number)
                    extraction += 1
                else:
                    print('[Fail] Test3 : 추출된 번호와 비슷합니다. 재 추출합니다.')
                    print(number)

            else:
                print('[Fail] Test2 : 이전에 당첨된 번호와 비슷합니다. 재 추출합니다.')
        else:
            print('[Fail] Test1 : 적합하지 않은 숫자입니다. 재 추출합니다.')
        if extraction == count:
            break
    print('추출완료')
    for i in result:
        print(i)
    return True