import numberLogManger

def check_number(number):
    if sum(number) < 20 or sum(number) > 200: return False
    if max(number) <= 15: return False
    if min(number) >= 15: return False
    counting = 0
    even = 0
    odd = 0
    remind = 0
    counting2 = [0,0,0,0,0]
    gap = []
    end_count = [ 0 for i in range(10)]
    for i in number:
        if remind != 0 and (i - remind) == 1:
            counting += 1
            remind = i
        elif remind != 0:
            counting = 0
            gap.append(i - remind)
            remind = i
        else: remind = i

        if i%2 == 0: even += 1
        else: odd += 1
        temp = str(i)
        end_count[int(temp[len(temp)-1])] += 1
        counting2[i//10] += 1
    if counting > 3 or even > 4 or odd > 4: return False
    gap = list(set(gap))
    if len(gap)==1:
        return False
    if max(end_count) > 2 or max(counting2) > 3:
        return False
    return True

def check_number_and_log(number):
    pre_number = numberLogManger.get_number()
    for i in pre_number:
        count = 0
        for j in i:
            if int(j) in number:
                count += 1
            if count > 4:
                return False
    return True
def check_number_and_extraction(number, extraction):
    for i in extraction:
        count = 0
        for j in i:
            if int(j) in number:
                count += 1
            if count > 4:
                return False
    return True