# Даны три целых числа. Определите, сколько среди них совпадающих. 
# Программа должна вывести одно из чисел: 3 (если все совпадают), 
# 2 (если два совпадает) или 0 (если все числа различны).

# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#     print(1)

a = int(input('1 - '))
b = int(input('2 - '))
c = int(input('3 - '))
arr = [a, b, c]
count = [0, 0, 0]
for i in range(2):
    for j in range(i, 3):
        if arr[i] == arr[j]:
            count[i] += 1
k = max(count)
if k == 1:
    print(0)
else:
    print(*count)
    print(k)
