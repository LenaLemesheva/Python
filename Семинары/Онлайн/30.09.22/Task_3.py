# Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.

from datetime import *


def k():
    return(datetime.now().microsecond)
a = int(input("Введите размерность: "))
res = int(k()/10 ** (6 - a))
print(res)
