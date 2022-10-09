# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

k = int(input('Введите число k - '))
fib1 = fib2 = 1
list = [fib1, fib2]
for i in range(2, k):
    fib1, fib2 = fib2, fib1 + fib2
    list.append(fib2)
fib1 = fib2 = 1
for i in range(-k, 1):
    fib1, fib2 = fib2, fib1 - fib2
    list.insert(0, fib2)  # добавили 0
print(list)


n = 8
fib = [0, 1]
for i in range(2, n + 1):
    fib.append(fib[-1] + fib[-2])
for i in range(n):
    # fib = [fib[1] - fib[0] + fib]
    fib.insert(0, fib[1] - fib[0])
print(fib)
