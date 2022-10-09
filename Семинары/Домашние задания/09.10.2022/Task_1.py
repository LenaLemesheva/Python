# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Пример:
# привет забвение пока   -    привет пока

text = input('Введите текст - ')
print(text)
res_text = list(filter(lambda x: 'абв' not in x, text.split()))
print(res_text)
