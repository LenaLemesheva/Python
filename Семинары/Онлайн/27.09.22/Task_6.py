# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# s = input('введите буквы: ')
# s1 = input('введите буквы: ')
# print(s.count(s1))

from itertools import count


s = input('введите буквы: ')
s1 = input('введите буквы: ')
count = 0
i = 0
while i < len(s):
    if s[i:i + len(s1)] == s1:
        count += 1
        i += len(s1)
    else:
        i += 1
print(count)
