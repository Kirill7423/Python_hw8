# Задача 38: Дополнить телефонный справочник возможностью изменения и 
# удаления данных. Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных

# Чтение файла
def readall(nm):
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            print(line.strip())


# Добавление информации
# def write_1(nm):
#     str_new1 = input('Фамилия: ')
#     str_new2 = input('Имя: ')
#     str_new3 = input('Отчество: ')
#     str_new4 = input('Телефон: ')
#     str_new = '\n' + str_new1 + ', ' + str_new2 + ', ' + str_new3 + ', ' + str_new4
#     with open(nm, 'a', encoding='utf8') as txt_file:
#         txt_file.write(str_new)


# Поиск по характеристике
# def find_item(nm):
#     item = input('Характеристика: ')
#     with open(nm, 'r', encoding='utf8') as txt_file:
#         for line in txt_file:
#             if item.lower() in line.lower():
#                 print(line.strip())

# def find_item_2(nm):
#     item = input('Что ищем: ')
#     item_type = int(input('Введите номер (0 - фамилия, 1 - имя, 2 - Отчество, 3 - Телефон): '))
#     with open(nm, 'r', encoding='utf8') as txt_file:
#         for line in txt_file:
#             line = line.split(', ')
#             if item.lower() in line[item_type].lower():
#                 print(*line)


# Сортировка списка по столбцу
# def sort_data(nm): 
#     list_1 = []
#     item_type = int(input('Введите номер (0 - фамилия, 1 - имя, 2 - Отчество, 3 - Телефон): '))
#     with open(nm, 'r', encoding='utf8') as txt_file:
#         for line in txt_file:
#             line = line.split(', ')
#             list_1.append(line)
#         list_1.sort(key = lambda person: person[item_type])
#     with open(nm, 'w', encoding='utf8') as txt_file:
#         for line in list_1:
#             line = ', '.join(line)
#             txt_file.writelines(line)



# Изменение данных в справочнике
def change_item(nm):
    list_2 = []
    item = input('Что будем заменять? ')
    item_new = input('Новое значение ')
    item_type = int(input('Введите номер (0 - фамилия, 1 - имя, 2 - Отчество, 3 - Телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                line[item_type] = item_new
                list_2.append(line)
            else:
                list_2.append(line)

    with open(nm, 'w', encoding='utf8') as txt_file:
        for line in list_2:
            line = ', '.join(line)
            txt_file.writelines(line)


# Удаление данных
def del_item(nm):
    list_2 = []
    item = input('Что нужно удалить? ')
    del_item = ' '
    item_type = int(input('Введите номер (0 - фамилия, 1 - имя, 2 - Отчество, 3 - Телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                line[item_type] = del_item
                list_2.append(line)
            else:
                list_2.append(line)

    with open(nm, 'w', encoding='utf8') as txt_file:
        for line in list_2:
            line = ', '.join(line)
            txt_file.writelines(line)


readall('data.txt')
# write_1('data.txt')
# print(find_item('data.txt'))
# find_item_2('data.txt')
# sort_data('data.txt')

change_item('data.txt')
del_item('data.txt')