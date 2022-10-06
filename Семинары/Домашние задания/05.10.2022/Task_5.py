# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')
file3 = open('file3.txt', 'w')
ist1 = file1.readline()
ist2 = file2.readline()
for i in range(len(ist1)):
    if ist1[i-1] != '*':
        if ist1[i].isnumeric():  # из строки выбираю числа
            file3.write(str(int(ist1[i])+int(ist2[i])))
        else:
            file3.write(str(ist1[i]))
    else:
        file3.write(str(ist1[i]))
file1.close()
file2.close()
file3.close()
