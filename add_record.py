import csv
from interface import *
from logger import log


def add_row(user_dict):
    results = []
    fieldnames = ['id', 'ФИО', 'Факультет', 'Специализация', 'Год обучения',
                  'Средний бал', 'Куратор', 'Кол-во курсов']

    with open('Book5.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(user_dict)

    with open('Book5.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            results.append(row)

    log('Добавление строки')

    return results



if __name__ == '__main__':
    user_dict = get_dict()
    results = add_row(user_dict)
    print_results(results, 'База данных студентов')