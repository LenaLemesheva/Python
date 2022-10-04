# Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.

a = int(input('Введите первое число - '))
b = int(input('Введите второе число - '))
if a > b:
    num = a
else:
    num = b
trigger = True
while trigger == True:
    if (num % a) == 0 and (num % b) == 0:
        trigger = False
    else:
        num += 1
print(num)
