from controller import to_do
from interface import print_results

if __name__ == '__main__':

    answer = 0
    if_first_time = True

    while answer != 5:

        if if_first_time:
            with open('Book5.csv', 'r', encoding='utf-8') as f:
                text = f.readlines()
            print_results(text, 'Перед вами база данных студентов')

        answer = to_do()
        if_first_time = False

