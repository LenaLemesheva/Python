# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: 
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: 
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW


txt = input('Введите текст для кодировки - ')


def compression(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res


def recovery(text):
    number = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            res = res + text[i] * int(number)
            number = ''
    return res


print(f'Текст после кодировки - {compression(txt)}')
print(f'Текст после дешифровки - {recovery(compression(txt))}')
