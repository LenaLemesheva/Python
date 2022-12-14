# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД)
# двух чисел. Вычислите и напечатайте наибольший общий делитель для списка натуральных 
# чисел. Ввод чисел продолжается до ввода пустой строки.
# Входные данные
# 36
# 12
# 144
# 18
# Выходные данные
# 6

import math
from functools import reduce

sp = list(map(int, input('Введите числа через пробел - ').split()))
print(reduce(math.gcd, sp))
