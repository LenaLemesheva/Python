# Даны два целых числа A и В, A>BA>B. Выведите все нечётные числа от A до B 
# включительно, в порядке убывания. В этой задаче можно обойтись без инструкции if.

# a = int(input('Введите первое число - '))
# b = int(input('Введите второе число - '))
# b = b + (b + 1) %2
# k = []
# for i in range(b, a + 1, 2):
#     k.append(i)
# k = k[:: -1]
# print(*k)

a = int(input())
b = int(input())
for i in range(a - (a + 1) % 2, b - b % 2, -2):
#    print(i, end=' ') # в строку
    print(i, end='\n')  # в столбец
