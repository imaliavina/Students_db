import csv
from interface import print_results
from logger import log


def search(element):
    results = []
    fieldnames = ['id', 'ФИО', 'Факультет', 'Специализация', 'Год обучения',
                  'Средний бал', 'Куратор', 'Кол-во курсов']

    with open('Book5.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            flag = False
            for v in row.values():
                if element in v:
                    flag = True
            if flag:
                results.append(row)

    log(f'Поиск по элементу {element}')
    if len(results) == 0:
        print('Нет строки, содержащей этот элемент')

    return results



if __name__ == '__main__':
    results = search('Артем')
    print_results(results, 'Результаты поиска:')