# Задайте строку из набора чисел. Напишите программу, которая покажет 
# большее и меньшее число. В качестве символа-разделителя используйте пробел.

sp = set(input('Введите числа через пробел - ').split())
print(sp)
print('max = ', max(sp), ' ', 'min = ', min(sp))
