# Дан список чисел. Выведите все элементы списка, 
# которые больше предыдущего элемента.

# lst = [1, 2, 5, 6, 7, 2, 3, 4, 6]
# for i in range(1, len(lst)):
#     if lst[i] > lst[i - 1]:
#         print(lst[i], end=" ")

ist = [int(i) for i in input("Введите числа через пробел: ").split()]
for i in range(0, len(ist) - 1):
    if ist[i] < ist[i+1]:
        print(ist[i+1])
