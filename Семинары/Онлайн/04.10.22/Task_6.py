# Дан текст: в первой строке задано число строк, далее идут сами строки. 
# Выведите слово, которое в этом тексте встречается чаще всего. 
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# Пример:
# 1                                     -       banana
# apple orange banana banana orange

# a = 'apple orange banana banana orange'
# a = a.split()
# b = {}
# max = 0
# word = "ZZZZZZ"
# for i in range(len(a)):
#     if a[i] in b.keys():
#         b[a[i]] += 1
#         if (b[a[i]]) > max:
#             max = b[a[i]]
#     else:
#         b[a[i]] = 1

# for elem in b:
#     if (b[elem] == max) and (elem < word):
#         word = elem
# print(word)

counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
         
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))
