# В единственной строке записан текст. Для каждого слова из данного 
# текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.
# Пример:
# one two one tho three   -   0 0 1 0 0.

# Вариант 1.

text = 'one two one tho three'
text = text.split()
double = {}
for i in text:
    if i in double:
        double[i] += 1
        print(double[i], end=' ')
    else:
        double[i] = 0
        print(double[i], end=' ')
for key in double:
    if double[key] > 0:
        print(key, 'Встречается более 1 раза')


# Вариант 2.

counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
