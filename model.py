import csv

from view import creating_info as info

def writing_csv(info): # создание файла csv
    with open ('data.csv', 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]},{info[3]}\n')

# 1 - показать все

def data_open():
    with open('data.csv', encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=',')
        return list(file_csv)
        
# 2 - добаавить запись

def add_info(lst):
    with open('data.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(lst)

# 3 - удалить запись

def del_info(index):
    list_csv = data_open()
    del list_csv[index]
    with open('data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for row in list_csv:
            writer.writerow(row)

# 4 - обновление записи телефона

def update_info(index, tel):
    list_csv = data_open()
    list_csv[index][3] = tel
    with open('data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for row in list_csv:
            writer.writerow(row)

  # 5 - обновление фамилии

def update_surname(index, surname):
    list_csv = data_open()
    list_csv[index][0] = surname
    with open('data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for row in list_csv:
            writer.writerow(row)          


def export_csv_txt():     # 6 экспорт из csv в txt
    list_csv = data_open()
    for i in list_csv:
        s = ' '.join(i)
        with open('data_2.txt', 'a', encoding='utf-8') as f:
            f.writelines(s + '\n')