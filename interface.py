def hello():
    answer = int(input('Выберите действие:\n1 - Поиск\n2 - Добавление\n'
                       '3 - Удаление\n4 - Редактирование\n5 - Выход\n'))
    return answer


def get_dict():
    fieldnames = ['id', 'ФИО', 'Факультет', 'Специализация', 'Год обучения',
                  'Средний бал', 'Куратор', 'Кол-во курсов']
    user_dict = {}

    print('Введите данные в данном порядке:')
    for each in fieldnames:
        user_dict[each] = input(f'{each} : ')

    return user_dict


def get_element():
    element = input('Введите элемент:')
    return element


def print_results(results, message):
    if len(results) > 0:
        print(message)
    for _ in results:
        print(_)

