from interface import hello
from interface import *
from add_record import add_row
from search_record import search
from edit_record import edit_row
from delete_record import remove_row


def to_do():

    answer = hello()

    if answer == 1:
        element = get_element()
        results = search(element)
    elif answer == 2:
        user_dict = get_dict()
        results = add_row(user_dict)
    elif answer == 3:
        element = get_element()
        results = remove_row(element)
    elif answer == 4:
        element = get_element()
        results = edit_row(element)
    elif answer == 5:
        pass

    if answer != 5:
        print_results(results, 'База данных студентов')

    return answer




if __name__ == '__main__':
    to_do()