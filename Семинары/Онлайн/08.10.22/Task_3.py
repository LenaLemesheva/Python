# Напишите функцию triangle(a, b, c), которая принимает на вход 
# три длины отрезков и определяет, можно ли из этих отрезков составить треугольник. 
# Пример:
# triangle(1, 1, 2)   -   Это не треугольник
# triangle(7, 6, 10)  -   Это треугольник

a = int(input())
b = int(input())
c = int(input())


def triangle(a, b, c):
    flag = False
    if (a+b) > c and (a+c) > b and (c+b) > a:
        flag = True
    return 'yes' if flag else 'no'


print(triangle(a, b, c))
