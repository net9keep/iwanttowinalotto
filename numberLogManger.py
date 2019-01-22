import csv
path = "/Users/achaean/Desktop/number_log.csv"
def read_number_log():
    file = open(path, 'r', encoding='utf-8', newline='')
    file_csv = csv.reader(file)
    return file_csv
def add_number(number):
    file = open(path, 'a', encoding='utf-8', newline='')
    file_csv = csv.writer(file)
    if file_csv.writerow(number):
        print('[Success] Log is update')
    else:
        print('[Fail] The Log file have been problem')

def get_number():
    file_csv = read_number_log()
    number_list = []
    for i in file_csv:
        number_list.append(i)
    return number_list