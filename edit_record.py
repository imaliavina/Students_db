import csv
from interface import *
from logger import log


def edit_row(element):
    results = []

    fieldnames = ['id', 'ФИО', 'Факультет', 'Специализация', 'Год обучения',
                  'Средний бал', 'Куратор', 'Кол-во курсов']

    with open('Book5.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)

        for row in reader:
            flag = False
            for value in row.values():
                if element in value:
                    row_to_edit = row
                    flag = True
            if not flag:
                results.append(row)

    print(row_to_edit)

    new_key = input('Что отредактировать? (Ключ - ФИО, Факультет и т.д.)')
    new_value = input('Введите новое значение:')

    row_to_edit[new_key] = new_value
    print(row_to_edit)
    results.append(row_to_edit)

    with open('Book5.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(results)

    log('Редактирование строки')

    return results


if __name__ == '__main__':
    element = get_element()
    results = edit_row(element)
    print_results(results, 'База данных студентов')