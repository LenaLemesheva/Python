# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.
# Пример:
# k = 2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


k = int(input('Введите коэффициент k - '))
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))
if a != 0:
    member1 = (str(a) + 'x**' + str(k))
else:
    member1 = (str())
if b != 0:
    member2 = (str(b) + 'x')
else:
    member2 = (str())
if c != 0:
    member3 = (str(c))
else:
    member3 = (str())
print((member1), '+', (member2), '+', (member3), '= 0')

polynomial = [member1, '+', member2, '+', member3, ' = 0']
data = open('file.txt', 'a')
data.writelines(polynomial)
data.write('\n')
data.close()
