# Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.

# from datetime import *


# def k():
#     return(datetime.now().microsecond)
# a = int(input("Введите размерность: "))
# res = int(k()/10 ** (6 - a))
# print(res)

from datetime import datetime


def num_random(n):
    number = datetime.now().microsecond
    return number % n


print(num_random(100))
