# Удалить вторую цифру трёхзначного числа.

# a = 123
# print(a // 100 * 10 + a %10)

# number = 123
# n1 = number // 100
# n2 = number % 10
# res = n1 * 10 + n2
# print(res)

# number = str(123)
# print(number[0] + number[2])

number = list(str(123))
number.remove('2')
print(number)
