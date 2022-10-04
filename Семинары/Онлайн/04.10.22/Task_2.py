# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#         1. с помощью математических формул нахождения корней квадратного уравнения
#         2. с помощью дополнительных библиотек Python

# Вариант 1.

# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# c = int(input('Введите c: '))
# D = b ** 2 - (4 * a * c)
# if D > 0:
#     x1 = (-b + D ** 0.5) / (2 * a)
#     x2 = (-b - D ** 0.5) / (2 * a)
#     print(round((x1), 3), round((x2), 3))
# elif D == 0:
#     x = -(b / (2 * a))
#     print(round((x), 3))
# else:
#     print('Вещественных корней нет')

# Вариант 2.

from math import sqrt

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
D = b ** 2 - (4 * a * c)
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(round((x1), 3), round((x2), 3))
elif D == 0:
    x = -(b / (2 * a))
    print(round((x), 3))
else:
    print('Вещественных корней нет')
