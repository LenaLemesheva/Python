# Реализуйте алгоритм перемешивания списка (метод random.shuffle 
# использовать нельзя, но другие методы из библиотеки random - можно).

import random
list1 = [1, 2, 3, 4, 5]
print ('Исходный список - ' + str(list1))
list2 = random.sample(list1, len(list1))
print ('Перемешанный список - ' +  str(list2))
