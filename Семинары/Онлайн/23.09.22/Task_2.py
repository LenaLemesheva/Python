# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
#        ◦ 1, 4, 8, 7, 5 -> 8
#        ◦ 78, 55, 36, 90, 2 -> 90

# m = 0
# for i in range(5):
#     x = int(input())
#     if m < x : m = x
# print(m)

sp = list()
for i in range(5):
    x = int(input())
    sp.append(x)
print(max(sp))
print(min(sp))
print(sum(sp))
