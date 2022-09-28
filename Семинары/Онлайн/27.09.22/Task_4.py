# Напишите программу, которая проверяет пятизначное число на палиндром.

# paltus = input('Введите число - ')
# if paltus[:2] == paltus[:2:-1]:
#     print('палиндром')
# else:
#     print('не палиндром')

# number = '123215'
# palindrome = True
# for i in range(len(number) // 2):
#     if number[i] != number[-i-1]:
#         palindrome = False
#         break
# if palindrome:
#     print('Палиндром')
# else:
#     print('Не палиндром')

number = '12321'
print(number == number[::-1])
