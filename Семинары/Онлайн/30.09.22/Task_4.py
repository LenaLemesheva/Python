# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
# Например: 12        -    да.
#           Строка1
#           Строка2
#           Строка3
#           Строка45
#           Стр12ка

# lst = ['12', 'Строка1', 'Строка2', 'Строка3', 'Строка45', 'Стр12ка']
# a = str(2)
# k = False
# for i in lst:
#     if a in i:
#         k = True
# print(k)

a = '123'
lst = ['Строка1', 'Строка2', 'Строка3', 'Строка45', 'Стр12ка']
count = 0
for word in lst:
    if a in word:
        count += 1
print('Да') if count > 0 else print('Нет')
