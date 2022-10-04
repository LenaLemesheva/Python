# В единственной строке записан текст. Для каждого слова из данного 
# текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.
# Пример:
# one two one tho three   -   0 0 1 0 0.

# Вариант 1.

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

# Вариант 2.

counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
