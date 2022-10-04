# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом 
# к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.
# Пример:
# 3                 -         Bye
# Hello Hi Bye Goodbye List Array Goodbye
# Bye Goodbye
# List Array
# Goodbye

# vocab = {}
# text = open('text.txt', 'r')
# for line in text:
#     a = line.split()
#     if len(a) == 2:
#         vocab[a[0]] = a[1]
#     if len(a) == 1:
#         word = a[0]
# text.close()
# print (f"Ищем синоним слова: {word}")
# for k, v in vocab.items():
#     if v == word:
#         print(k)
#     if k == word:
#         print(v)

n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])
