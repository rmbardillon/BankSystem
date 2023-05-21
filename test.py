import csv
import os


def add_header(file, header):
    if os.path.isfile(file):
        size = os.path. getsize(file)
        if size == 0:
            with open(file, 'w', encoding='UTF8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
    else:
        with open(file, 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)


def add_test_cases(header, case_number, wind1, wind2, pi_s_total):
    add_header('test_cases.csv', header)
    data = [case_number, wind1, wind2, pi_s_total]
    with open('test_cases.csv', 'a', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


wind_case_number = 1
a_total = 0
b_total = 0
pi_s_total = 0
num = 1
W1=[0, 0.6, 1.00]
W2=[0, 0.6, 1.00]
test_cases_header = ['Case', 'Wind 1', 'Wind 2', 'Pi_S_Total']
for a in W1:
    if a == 0:
        a_total += 0.141359131 ** 2
    elif a == 0.6:
        a_total += 0.126437827 ** 2
    elif a == 1:
        a_total += 0.062560686 ** 2
    for b in W2:
        if b == 0:
            b_total += 0.141359131 ** 2
        elif b == 0.6:
            b_total += 0.126437827 ** 2
        elif b == 1:
            b_total += 0.062560686 ** 2
        pi_s_total = (a_total + b_total) ** .5
        print(f'{[a,b]} {pi_s_total}')
        add_test_cases(test_cases_header, wind_case_number,a,b, pi_s_total)
        wind_case_number += 1
        pi_s_total = 0
        b_total = 0
    a_total = 0
