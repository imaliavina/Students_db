import csv
from interface import print_results
from logger import log


def remove_row(element):
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
            if not flag:
                results.append(row)
            else:
                print(row)

    with open('Book5.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(results)

    log('Удаление строки')

    return results



if __name__ == '__main__':
    results = remove_row('Пуффендуй')
    print_results(results, 'База данных студентов')