# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = float(input('Введите число с заданной точностью - '))
print(f'Число Пи равно - ', round(pi, str(d).count('0')))
