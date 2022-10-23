
def write_menu(): # меню для начала работы
    print('Выберите цифру 1, если хотите начать работу. В противном случае, нажмите любую цифру: ')
    return int(input('Введите цифру: '))


def number_entries(): # сколько записей сделать в информационной системе
    print('Информационной системы пока нет, её нужно создать.')
    num = int(input('Начнем! Введите количество записей, которые Вы хотите сделать: '))
    return num


def creating_info(): # создание записи по одному человеку
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    second_name = input('Введите отчество: ')
    info.append(second_name)
    tel = input('Введите номер телефона: ')
    info.append(tel)
    return info


def show_menu(): # меню в случае, если база уже существует
    print('Информационная система существует. Что будем делать дальше?')
    print('1 - показать все')
    print('2 - добавить запись')
    print('3 - удалить запись')
    print('4 - изменить телефон')
    print('5 - изменить фамилию')
    print('6 - перенести базу в формат txt')
    return int(input('Введите цифру: '))


def delite():
    print('Введите номер строки для удаления: ')
    return int(input())


def change_tel():
    print('Введите номер строки для изменения: ')
    print('Введите новый номер телефона: ')
    return int(input()), input()
    

def show_res(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))


def add_info():
    print('Введите ФИО и телефон через пробел: ')
    in_info = input().split()
    return in_info


def change_surname():
    print('Введите номер строки для изменения: ')
    print('Введите новую фамилию: ')
    return int(input()), input()