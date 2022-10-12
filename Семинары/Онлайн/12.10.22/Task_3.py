# Преобразовать набор списков (используя функцию zip)
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор 
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
# и потом вернуть в исходное состояние
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

# from itertools import zip_longest  # Функция zip_longest работает аналогично встроенной функции zip
                                   # но не останавливается на самом коротком итерируемом объекте

from itertools import zip_longest


users = ['user1','user2','user3','user4','user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]
temp = [list(i) for i in zip(users, ids, salary)]
# temp = [list(i) for i in zip_longest(users, ids, salary, fillvalue='')]  # если список разной длины
# for i in range(len(temp)):  # убираем пустоты
#      temp[i] = list(filter(lambda x: x, temp[i]))
print(temp)
print(list(zip(*temp))) # * для распаковки итерируемых объектов в список/кортеж
