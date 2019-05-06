import csv
import re


def get_data(files):
    pattern_1 = re.compile('Изготовитель системы')
    pattern_2 = re.compile('Название ОС')
    pattern_3 = re.compile('Код продукта')
    pattern_4 = re.compile('Тип системы')

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'],
                 os_prod_list, os_name_list, os_code_list, os_type_list]


    for file in files:
        with open(file, 'r') as f:
            for line in f:
                if re.match(pattern_1, line):
                    os_prod_list.append(re.search(r'[A-Z]+\n', line).group(0).rstrip('\n'))
                if re.match(pattern_2, line):
                    os_name_list.append(re.split(r':[\s]+', line)[1].rstrip('\n'))
                if re.match(pattern_3, line):
                    os_code_list.append(re.search(r'[\d].+\n', line).group(0).rstrip('\n'))
                if re.match(pattern_4, line):
                    os_type_list.append(re.search(r'x.+\n', line).group(0).rstrip('\n'))


    return main_data

def write_to_csv(data):
    with open('main_data.csv', 'w') as result:
        result_writer = csv.writer(result)
        for row in data:
            result_writer.writerow(row)


files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
write_to_csv(get_data(files))