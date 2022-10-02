# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec_num = int(input('Введите число - '))
bin_num = ''
while dec_num != 0:
    bin_num += str(dec_num % 2)
    dec_num //=2
print('Его двоичным числом будет - ', bin_num[::-1])
