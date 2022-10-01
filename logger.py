from datetime import datetime as dt


def log(operation):
    time = dt.now()
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{time.hour} : {time.minute}   операция: {operation}\n')