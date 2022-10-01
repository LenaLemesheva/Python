# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

ist1 = [int(i) for i in input("Введите числа через пробел: ").split()]


def list_product_pairs(ist1):
    ist2 = []
    for i in range((len(ist1)+1)//2):
        ist2.append(ist1[i]*ist1[len(ist1)-1-i])
    return ist2


print(list_product_pairs(ist1))
