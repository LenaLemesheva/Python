# Даны два списка чисел. Найдите все числа, которые входят как в первый, 
# так и во второй список и выведите их в порядке возрастания.
# Пример:
# 1 3 2    -    2 3
# 4 3 2

ist1 = [int(i) for i in input("Введите числа первого списка через пробел: ").split()]
ist2 = [int(i) for i in input("Введите числа второго списка через пробел: ").split()]
new_ist = []
for i in ist1:
    for j in ist2:
        if i == j:
            if i not in new_ist:
                new_ist.append(i)
new_ist.sort() 
print(new_ist)
