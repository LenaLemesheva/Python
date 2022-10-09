# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# ist1 = list(map(float, input("Введите числа через пробел: ").split()))
# ist2 = [round(i % 1, 2) for i in ist1 if i % 1 != 0]
# print(max(ist2) - min(ist2))


spisok = [1.1, 1.2, 3.1, 5, 10.01]
sp_frac = [abs(i - int(i)) for i in spisok if int(i) != i]
print(sp_frac)
print(max(sp_frac) - min(sp_frac))
