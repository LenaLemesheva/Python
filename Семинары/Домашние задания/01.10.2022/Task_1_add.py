# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Пример:
# 1 5 2 2 2 4 - 4.

# Вариант 1

plenty = set(input('Введите числа через пробел - '))
print(plenty)
N = 0
for i in plenty:
    N += 1
print(N - 1) # чтобы убрать пробел

# Вариант 2

plenty = set(input('Введите числа без пробела - '))
print(plenty)
N = 0
for i in plenty:
    N += 1
print(N)
