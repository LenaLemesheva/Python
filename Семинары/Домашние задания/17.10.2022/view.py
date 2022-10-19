
from unittest import result


def choice():
    print('Телефонный справочник')
    result = int(input('Выберите 1 или 2: \n\
        1 - Внесите абонент\n\
        2 - Выход\n\
        Выберите пункт: '))
    return result