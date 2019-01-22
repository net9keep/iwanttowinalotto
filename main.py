import numberLogManger
import check_rule
import random
number_list = [i for i in range(1,46)]
extraction = 0
result = []
while True:
    number = random.sample(number_list, 6)
    number = sorted(number)
    if check_rule.check_number(number):
        print('[Success] Test1 : 적합한 숫자입니다.')
        if check_rule.check_log(number):
            print('[Success] Test2 : 적합한 숫자입니다.')
            print(number)
            result.append(number)
            extraction += 1
        else:
            print('[Fail] Test2 : 이전에 당첨된 번호와 비슷합니다. 재 추출합니다.')
            print(number)
    else:
        print('[Fail] Test1 : 적합하지 않은 숫자입니다. 재 추출합니다.')
        print(number)
    if extraction == 5:
        break
print('추출완료')
for i in result:
    print(i)
