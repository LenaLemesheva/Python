# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

N = int(input('Введите число - '))
sum = 0
n = 1
for i in range(1, N + 1):
        print(round(((1 + 1 / n) ** n), 2), end=' ')      
        sum = ((1 + 1 / n) ** n) + sum
        n += 1
        i += 1 
print('Сумма чисел равна - ', round((sum), 2))
