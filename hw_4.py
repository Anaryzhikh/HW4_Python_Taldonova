# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# a = float(input('Введите число: '))
# d = input('Введите точность округления: ')
# precision = 0
# d_split = d.split('.', 1)
# for i in d_split:
#     if len(i) > 1:
#         precision = i
# print(round(a, len(precision)))

# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

# def get_prime_factors(n):
#     factors = []
#     divisor = 2
#     while divisor <= n:
#         if n % divisor == 0:
#             factors.append(divisor)
#             n = n/divisor
#         else:
#             divisor += 1
#     return factors
#
# n = int(input('введите число: '))
# print(get_prime_factors(n))

# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# from random import random
#
# numbers = []
# for i in range(10):
#     numbers.append(int(random()*10))
# print(numbers)
# result = []
# for k in numbers:
#     if numbers.count(k) == 1: # считаем кол-во элементов i в списке
#         result.append(k)
# print(result)

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Смогла реаклизовать программу только через склеивание

with open('poly_1.txt', 'w', encoding='utf-8') as file:
    file.write('5*x^3 + 8*x^2')

with open('poly_2.txt', 'w', encoding='utf-8') as file:
    file.write('10*x^4 + 6*x^3')

with open('poly_1.txt', 'r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()

with open('poly_2.txt', 'r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')