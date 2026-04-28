# Пользователь вводит три числа. Найти сумму тех чисел,
# # которые делятся на 5. Если таких чисел нет, то вывести error.
#
# a = int(input("Введите первое число - "))
# b = int(input("Введите второе число - "))
# c = int(input("Введите третье число - "))
#
# if a % 5 == 0 and b % 5 == 0 and c % 5 == 0:
#     print(a+b+c)
#
# elif a % 5 == 0 and b % 5 == 0 and c % 5 != 0:
#     print(a+b)
#
# elif a % 5 != 0 and b % 5 == 0 and c % 5 == 0:
#     print(c + b)
#
# elif a % 5 == 0 and b % 5 != 0 and c % 5 == 0:
#     print(a + c)
#
# elif a % 5 != 0 and b % 5 != 0 and c % 5 == 0:
#     print(c)
#
# elif a % 5 == 0 and b % 5 != 0 and c % 5 != 0:
#     print(a)
#
# elif a % 5 != 0 and b % 5 == 0 and c % 5 != 0:
#     print(b)
#
# else:
#     print("error")
from itertools import count

# a = int(input("Введите первое число - "))
# b = int(input("Введите второе число - "))
# c = int(input("Введите третье число - "))

# for i in range(0, 100, 2):
#     print(i)


# a,b,c = 10,20,30
# b = int(input("введите второе число - "))
# c = int(input("введите третье число - "))
# print(max(a,b,c))
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# hello = "Привет"
# print(hello[1:5])

# age = 20
# print( "Взрослый" if age >= 18 else "ребенок" )

# Написать программу, которая складывает
# все числа находящиеся в массиве


# a = [1,2,3,4,5]
# num = 0
# for i in a:
#     num += i
# print(num)


# def sum(a,b):
#     c=a+b
#     return c
# # num = sum(10,20)
# print(sum(10,20))

# a = 0
# k = 20
# while a < k:
#     print(a)
#     a += 1

# Посчитайте НОД двух чисел (алгоритм Евклида)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# original_a = a
# original_b = b
#
#
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
#
# nod = a
#
# print(f"Нод чисел {original_a} и {original_b} = {nod}")

# Посчитайте НОК двух чисел


# a = int(input("Введите первое число - "))
# b = int(input("Введите второе число - "))
#
# x = a
# y = b
#
# while x != y:
#     if x > y:
#         x = x - y
#     else:
#         y = y - x
#
# nod = x
#
# nok = (a * b) // nod
#
# print(f"НОК чисел {a} и {b} = {nok}")

# Проверьте, является ли число простым

# import math
#
# n = int(input("Введите число n - "))
#
# if n <= 1:
#     print("Не простое")
#     exit()
#
# simple = True
#
# for i in range(2, int(math.sqrt(n)) + 1):
#     if n % i == 0:
#         simple = False
#         break
#
# if simple == True:
#     print("Простое")
# else:
#     print("Не простое")


# while True:
#     out = input("Введите Выход, Введите С для продолжение - ")
#
#     if out.lower() == "выход": break
#
#     numbers = int(input("Введите число - "))
#     numbers_two = int(input("Введите число - "))
#     oper = input("Введите *,/,+,- ")
#
#     if oper == "*":
#         print(numbers * numbers_two)
#
#     elif oper == "/":
#         if numbers_two == 0:
#             print("делить на ноль нельзя")
#
#         else:
#             print(numbers / numbers_two)
#
#     elif oper == "+":
#         print(numbers + numbers_two)
#
#     elif oper == "-":
#         print(numbers - numbers_two)


# import  random
#
# target = random.randint(1, 10)
#
# while True:
#
#     numbers = int(input("Угадай число - "))
#
#     if numbers > target:
#         print("Введите число меньше")
#
#     elif numbers < target:
#         print("Введиет число больше")
#
#     elif numbers == target:
#         print("Число Угадано")
#
#         break

# Создайте список из n объектов.
# Добавьте В начало списка объект и удалите 1 объект из конца

# spisok = [1,2,3,4,5,6]
# spisok.append(1)
# spisok.pop(5)
# print(spisok)


# factr = int(input("Введите n число - "))
#
# result = 1
#
# for i in range(1, factr + 1):
#     result *= i
# print(result)


# При разработке текстового интерфейса для контроллера необходимо реализовать цикл прослушивания команд.
# Программа должна непрерывно запрашивать и выводить вводимые строки.
# Цикл опроса прерывается только при получении команды остановки - слова "хватит".


#
# while True:
#     users = input("Введиете слово - ")
#
#     if users.lower() == "хватит":
#         break
#
#     else:
#         print(f"Эхо: {users}")

# Система последовательно считывает числовые значения (например, показания датчиков).
# Необходимо накапливать общую сумму входящих данных до тех пор,
# пока не поступит сигнал обрыва связи или завершения передачи - 0.
# После этого система выводит итоговую сумму.

# numb = int(input("Введите число(0 - для остановки) - "))
# total = 0
# while numb != 0:
#     total += numb
#     numb = int(input("Введите число(0 - для остановки) - "))
# print(total)

# Для синхронизации процессов требуется сгенерировать
# последовательность четных чисел от 2 до заданного предела N.
# Напишите цикл, который выводит эти значения в строку, имитируя ровные такты.


# start = 2
# end = int(input("Введие n число - "))
# while start < end:
#     print(start, end=" ")
#     start += 2


# print("sdsd","ssasd", sep="*")

# start = 2
# end = 24
#
# for i in range(start,end,start):
#     print(i, end=" ")


# 1. Требуется написать логику верификации длины PIN-кода. Запрашивайте у пользователя ввод до тех пор,
# пока длина введенной последовательности не будет строго соответствовать стандарту - от 4 до 6 символов включительно.
# При ошибке выводите (неверный формат).
# Подсказка - глобальная переменная пустая строка и в цикле та же переменная, куда вводить пароль


# users = ""
# while True:
#     users = input("Введите Pin-код - ")
#     if len(users) >= 4 and len(users) <= 6:
#         print("Pin-код подходит")
#         break
#     else:
#         print("неверный формат")


# 2. Перед запуском основного процесса необходимо выждать определенное время.
# Запросите стартовое значение N (начало отсчёта) и реализуйте цикл обратного отсчета до единицы
# (!!!!) с шагом в 1.
# По завершении цикла выведите "старт".

# start_value = int(input("Введите стартовое значение: "))
# end = 0
# while end < start_value:
#     print(start_value)
#     start_value -= 1
# print("Старт")


# Реализуйте защитный механизм для критической операции.
# Программа должна задавать вопрос "Вы уверены? (да/нет)" и блокировать дальнейшее выполнение (повторять запрос),
# пока не будет получен строго точный ответ "да" или "нет".


# answer = ""
# block = ["да", "нет"]
# while answer not in block:
#     answer = input("Вы уверены? (да/нет): ").lower()
# print(answer)

# answer = ""
# while True:
#     answer = input("Вы уверены? (да/нет): ").lower()
#     if answer == "да" or answer == "нет":
#         break
# print(answer)

# Выведите последовательность степеней двойки, начиная с 1.
# Каждая итерация цикла должна умножать текущее значение на 2.
# Процесс останавливается, как только значение превысит порог в 1000.


# val = 1
# while val <= 1024:
#     print(val, end=" ")
#     val *= 2

# Реализуйте сборку слова посимвольно.
# Программа запрашивает по одной букве и добавляет ее в общий буфер-строку.
# Цикл должен продолжаться до тех пор, пока буфер не заполнится ровно до 5 символов.


# boffer = ""
#
# while len(boffer) < 5:
#     users = input("Введите символ - ")
#     boffer += users[0]
# print(boffer)


# Задача 1
# Программа запрашивает у пользователя количество калорий в блюде.
# Пользователь вводит числа одно за другим. Как только общая сумма калорий превысит лимит (например, 2000),
# программа должна остановиться, вывести итоговую сумму и сказать,
# на сколько именно калорий был превышен лимит.

# limit = 2000
# total_calories = 0
# while total_calories <= limit:
#     user = int(input("Введиет число - "))
#     total_calories += user
# print(f"Количество калорий: {total_calories} ")
# print(f"Количество калорий привышен на: {total_calories - limit}")

# Задача 2
# У тебя есть цель — накопить на новый монитор (допустим, 15 000 рублей).
# Каждый "день" (каждую итерацию цикла) ты вносишь случайную сумму от 100 до 500 рублей.
# Цикл должен работать, пока сумма в копилке меньше цели.
# После каждой "внесенной" суммы программа должна печатать:
# "Сегодня внесено: [сумма], всего в копилке: [сумма]".
# В конце выведи, за сколько дней удалось накопить. (Можно использовать random для удобства)


# import  random
# day = 0
# balance = 0
# limit = 15000
# while balance <= limit:
#     deposit = random.randint(100,500)
#     balance += deposit
#     day += 1
#     print(f"Сегодня внесено:  {deposit}, всего в копилке: {balance}")
# print(f"Накопили за: {day} дней")


# 1.Дана некоторая строка "1316351523610123123123". Найдите позицию первого нуля в строке.

# string =  "13016351523610123123123"
#
# count = 0
# for i in string:
#     if int(i) != 0:
#         count += 1
#     else:
#         print(count)
#         break

# 2. Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти.


# for num in range(10, 1001):
#     if (int(str(num)[0])+int(str(num)[1])) == 5:
#         print(num)


# 3.Дана некоторая строка: "'abcdeabc", очистите ее от дублей символов

# string = "abcdeabc"
#
# set = set(string)
# lst = list(set)
# lst.sort()
# print(lst)

# 4.Дан список с числами [1,2,3,-2,-3,5,-10,3,-14,6].
# Подсчитайте количество отрицательных чисел в этом списке.

# lst = [1,2,3,-2,-3,5,-10,3,-14,-2,6]
#
# count = 0
# for i in lst:
#     if i < 0:
#         count+=1
# print(f"количество отрицательных чисел - {count}")


# 5.  Дан список с числами. Оставьте в нем только положительные числа.

# lst = [1,3,4,5,6,7,-1,-2,2,-4]
#
# lst1 = []
#
# for i in lst:
#     if i >= 0:
#         lst1.append(i)
# print(lst1)

# 1. Даны два слова "Аня", "Ян".
# Проверьте, что последняя буква первого слова совпадает с первой буквой второго слова.


# while True:
#     name1 = input("Введите первое слово - ")
#     name2 = input("Введите второе слово - ")
#
#     if name1[-1].lower() == name2[0].lower():
#         print(f"Одинаковая буква эта - {name1[-1].lower()}")
#
#     stop = input("Введите 'Стоп': ")
#
#     if stop.lower() == "стоп":
#         print("Программа завершена")
#         break


# # 2. Дано число - 12345678245. Выведите в консоль количество четных цифр в этом числе.
#
# count = 0
# while True:
#     numbers = input("Введите число/Введите 0 для завершение - ")
#     if numbers == "0":
#         print("Программа завершена")
#         break
#     total = 0
#     for i in numbers:
#         n = int(i)
#         if n % 2 == 0:
#             count += 1
#             total += 1
#     print(f"Вывод количетсво четных чисел: {total}")
#     print(f"Вывод общее количество четных чисел: {count}")
#
#
#
# # 3.Дана некоторая строка 'abcde' Переведите в верхний регистр все нечетные буквы этой строки.

# str1 = input("Введите строку - ")
#
# str2 = ""
#
# for i,char in enumerate(str1):
#     if i % 2 == 1:
#         str2 += char.upper()
#
#     else:
#         str2 += char
#
# print(str2)


# 4. Дан некоторый список [1, 2, 3, 4, 5, 6] Поделите сумму элементов,
# стоящих на четных позициях, на сумму элементов, стоящих на нечетных позициях

# list1 = [1, 2, 3, 5, 5, 6, 8, 10]
#
# odd = 0
# even = 0
#
#
# for num in range(0, len(list1)):
#     if num % 2 == 0:
#         even += list1[num]
#
#     else:
#         odd += list1[num]
#
# result = even / odd
#
#
# print(f"четные позиции - {even}")
# print(f"нечетные позиции - {odd}")
# print(f"Результат - {result}")


# 4. Дан некоторый список [1, 2, 3, 4, 5, 6] Поделите сумму элементов,
# стоящих на четных позициях, на сумму элементов, стоящих на нечетных позициях

# list1 = [1, 2, 3, 5, 5, 6, 8, 10]
#
# even = list1[0::2]
# odd = list1[1::2]
#
# even_sum = sum(even)
# odd_sum = sum(odd)
#
# result = even_sum / odd_sum
#
# print(f"четные позиции - {even_sum}")
# print(f"нечетные позиции - {odd_sum}")
# print(f"Результат - {result}")


# 5. Дана некоторая строка с буквами и цифрами "абвг13гд34рп78".
# Получите список позиций всех цифр из этой строки.


# str1 = "абвг13гд34рп78"
#
# list1 = []
# count = 0
#
# for i in str1:
#     if i.isdigit():
#         list1.append(count)
#     count += 1
# print(list1)


# str1 = "абвг13гд34рп78"
#
# list1 = []
#
# for i,char in enumerate(str1):
#     if char.isdigit():
#         list1.append(i)
# print(list1)

# 1. Дан некоторый список с числами [1, 2, 3, 4, 5, 6]
# Слейте пары элементов вместе [12, 34, 56]

# list1 = [1, 2, 3, 4, 5, 6]
#
# list2 = []
#
# for num in range(0, len(list1), 2):
#     first = list1[num]
#     second = list1[num +1]
#     combo = int(str(first) + str(second))
#     list2.append(combo)
# print(list2)


# 1. Напишите программу, которая принимает на вход два числа a и b
# вычисляет сумму, разность и произведение для этих чисел и выводит текст в следующем формате:

# <число a> + <число b> = <сумма чисел a и b>
# <число a> - <число b> = <разность чисел a и b>
# <число a> * <число b> = <произведение чисел a и b>

# a = input()
# b = input()
#
# q = int(a) + int(b)
# r = int(a) - int(b)
# v = int(a) * int(b)
#
# print(f"{a} + {b} = {q}")
# print(f"{a} - {b} = {r}")
# print(f"{a} * {b} = {v}")


# a1 = input()
# d = input()
# n = input()
#
# a1 = int(a1)
# d = int(d)
# n = int(n)
#
# result = a1 + d * (n - 1)
#
# print(result)

# x_numbs = input()
# x = int(x_numbs)
#
# x1 = x
# x2 = x * 2
# x3 = x * 3
# x4 = x * 4
# x5 = x * 5
#
# result = f"{x1} --- {x2} --- {x3} --- {x4} --- {x5}"
#
# print(result)


# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)


# a = 82 // 3**2 % 7
# print(a)

# a = input()
# b = input()
# c = input()
#
# a = int(a)
# b = int(b)
# c = int(c)
#
# result = a * b ** (c - 1)
# print(result)

# a = input()
# centimeters = int(a)
#
# meters = centimeters // 100
#
# print(meters)

# user = input()
# user1 = input()
#
# pupils = int(user)
# Mandarins = int(user1)
#
# each = Mandarins // pupils
# remains = Mandarins % pupils
#
# print(each)
# print(remains)


# user = input()
#
# numbers = int(user)
#
# result = (numbers + 1) // 2
#
# print(result)

# total_minutes = int(input())
#
# watch = total_minutes // 60
# minutes = total_minutes % 60
#
# print(f"{total_minutes} мин - это {watch} час {minutes} минут.")


# place = int(input())
#
# compartment = (place + 3) // 4
#
# print(compartment)

# Задача 1. Напишите программу, определяющую число десятков и единиц в двузначном числе.
# Решение. Число единиц – это последняя цифра числа, число десятков – первая цифра. Чтобы
# получить последнюю цифру любого числа, нужно найти остаток от деления числа на 10
# Чтобы найти первую цифру двузначного числа, нужно поделить число нацело на 10.
# Программа, решающая поставленную задачу, может иметь следующий вид:


# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
#
# print('Число десятков =', first_digit)
# print('Число единиц =', last_digit)


# Задача 2. Напишите программу, в которой рассчитывается сумма цифр двузначного числа.

# num = int(input())
#
# last_digit = num % 10
# first_digit = num  // 10
#
# print("Сумма цифр =", last_digit + first_digit)

# Задача 3. Напишите программу, которая печатает число,
# образованное при перестановке цифр двузначного числа.


# num = int(input())
#
# last_digit = num % 10
# first_digit = num  // 10
#
# print("Искомое число =", last_digit * 10 + first_digit)

# Задача 4. Напишите программу,
# в которую вводится трехзначное число и
# которая выводит на экран его цифры (через запятую).

# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
#
# print(digit1, digit2, digit3, sep=',')
#
# Пример 1. Найти цифры двузначного числа

# num = int(input())
# first_num = num // 10
# second_num = num % 10
#
# print("Десятки =", first_num)
# print("Единицы =", second_num)


# Пример 2. Найти цифры трехзначного числа
# Условие:
# Пользователь вводит трехзначное число (например, 629).
# Программа должна вывести три цифры:
#
# сотни
# десятки
# единицы

# num = int(input())
# hundreds = num // 100
# tens = (num // 10) % 10
# units = num % 10
#
# print("Сотни =", hundreds)
# print("Десятки =", tens)
# print("Единицы =", units)

# Пример 3. Собрать число из цифр

# hundreds = int(input())
# tens = int(input())
# units = int(input())
#
# number = hundreds * 100 + tens * 10 + units
#
# print(number)

# tens = int(input())
# units = int(input())
#
# numbers = tens * 10 + units
#
# print(numbers)


# 4. Поменять местами десятки и единицы

# num  = int(input())
#
# new_numbers = (num % 10) * 10 + (num // 10)
#
# print(new_numbers)

# Напишите программу, которая рассчитывает
# сумму и произведение цифр положительного
# трёхзначного числа и выводит текст в следующем формате:


# num = int(input())
# hundreds = num // 100
# dozens = (num // 10) % 10
# units = num % 10
#
# suma = hundreds + dozens + units
# composition = hundreds * dozens * units
#
# print("Сумма цифр =", suma)
# print("Произведение цифр =", composition)


# 1. Основы:
# * Напиши функцию,
# которая принимает список чисел и возвращает сумму только чётных чисел.


# Напиши функцию, которая принимает список целых чисел и
# возвращает сумму только чётных чисел.

# def even(lst):
#     count = 0
#     for num in lst:
#         if num % 2 == 0:
#             count = count + num
#     return count
# result = even([1,2,3,4,5,6])
# result1 = even([10,15,20,25])
# result2 = even([1,3,5,7])
# result3 = even([])
# print(result)
# print(result1)
# print(result2)
# print(result3)


# def func(a, b=[]):
#     b.append(a)
#     return b
#
# print(func(1))
# print(func(2))
# print(func(3, []))
# print(func(4))

# Задача 1 (условия):
# Напиши функцию is_even(n), которая возвращает True,
# если число чётное, и False, если нечётное.

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# result = is_even(2)
# print(result)

# Задача 2 (цикл for):
# Напиши функцию sum_from_to(a, b),
# которая возвращает сумму всех целых чисел от a до b включительно.

# def sum_from_to(a,b):
#     total = 0
#     for i in range(a, b +1):
#         total = total + i
#     return total
# print(sum_from_to(2,4))

# Задача 3 (цикл while):
# Напиши функцию count_digits(n),
# которая считает количество цифр в целом положительном числе.

# def count_digits(n):
#     count = 0
#     while n > 0:
#         count += 1
#         n //= 10
#     return count
# result = count_digits(100)
# print(result)

# Задача 4 (списки и циклы):
# Напиши функцию reverse_list(lst), которая возвращает
# новый список с элементами в обратном порядке, не используя [::-1] и reverse().

# def reverse_list(lst):
#     new_lst = []
#
#     for i in range(len(lst)-1,-1,-1):
#         new_lst.append(lst[i])
#     return new_lst
# result = reverse_list([1,2,3,4,5])
# print(result)

# Задача 5 (функции и логика):
# Напиши функцию find_max(numbers),
# которая принимает список чисел и возвращает максимальное значение,
# не используя max(). Если список пустой — вернуть None.


# Дан список с числами [100, 10, 21, 323, 33, 45, 32255].
# Удалите из него числа, состоящие более чем из трех цифр.

# lst = [100, 10, 21, 323, 33, 45, 32255, 132334,334521,1242512]
#
# for i in lst.:
#     if i > 999:
#         lst.remove(i)
# print(lst)


# def sum(a,b):
#     return a + b
#
# print(sum(1,3))

# def check_age(age):
#     if age < 18:
#         return "Доступ закрыт"
#     return "Добро пожаловать"
# print(check_age(17))

# def a(num: int) -> int:
#     return num

# lst = [100, 10, 21, 323, 33, 45, 32255, 132334,334521,1242512]
#
# def num(lst):
#     for i in lst[:]:
#         if i > 999:
#            lst.remove(i)
#     return lst
# print(num(lst))


# def func(a):
#     return f"Привет! {a}"
#
# while True:
#     name_stop = (input("Введите: имя/Стоп - "))
#     if name_stop.lower() == "стоп":
#         break
#
#     print(func(name_stop))

# Написать функцию check_ping(ping).
# Если пинг меньше 50 - вернуть "Отлично". От 50 до 100 - "Нормально".
# Больше 100 - "Плохо".

# def check_ping(ping):
#     if ping < 50:
#         return "Отлично"
#
#     elif 50 < ping < 100:
#         return "Нормально"
#
#     else:
#         return "Плохо"
#
# while True:
#     print_ping = input("Введите ms(пинг)/Стоп - ")
#     if print_ping.lower() == "стоп":
#         break
#
#     print(check_ping(int(print_ping)))


# Дан список кодов ответов сервера: [200, 404, 200, 500, 404, 200].
# Написать функцию count_errors(codes), которая посчитает, сколько раз встретилась ошибка 404.


# def count_errors(codes):
#     count = 0
#     for i in codes:
#         if i == 404:
#            count += 1
#     return count
#
# lst = [200, 404, 200, 500, 404, 200, 404]
#
# print(count_errors(lst))


# Дан массив температур процессоров: [45, 80, 95, 50, 92].
# Написать функцию get_overheated(temps),
# которая вернет новый список, содержащий только температуры выше 90 градусов.

# def get_overheated(temps):
#     lst = []
#     for i in temps:
#         if i > 90:
#             lst.append(i)
#     return lst
# temperature = [45, 80, 95, 50, 92,98]
# print(get_overheated(temperature))

# Сервер каждую минуту генерирует текстовые сообщения (логи).
# Большинство из них - это обычная информация (INFO),
# но иногда случаются ошибки (ERROR) или критические сбои (CRITICAL).
# Нужно написать функцию, которая вытащит из общего массива только проблемные строки.
#


# def errors(log):
#
#     bad_logs = []
#     for i in log:
#         if "ERROR" in i or "CRITICAL" in i:
#             bad_logs.append(i)
#
#     return bad_logs
#
# server_logs = [
#     "INFO: Server started successfully",
#     "INFO: User admin logged in",
#     "ERROR: Database connection timeout",
#     "INFO: Data backup completed",
#     "CRITICAL: Memory usage at 99%",
#     "WARNING: Disk space is running low",
#     "ERROR: Failed to load config file"
# ]
#
# print(errors(server_logs))


# num = int(input())
# hundreds = num // 100
# dozens = (num // 10) % 10
# units = num % 10
#
# suma = hundreds + dozens + units
# composition = hundreds * dozens * units
#
# print("Сумма цифр =", suma)
# print("Произведение цифр =", composition)


# total_minutes = int(input())
#
# watch = total_minutes // 60
# minutes = total_minutes % 60
#
# print(f"{total_minutes} мин - это {watch} час {minutes} минут.")


# 1. Сервер записывает все попытки входа.
# Нужно написать функцию find_hackers(logs),
# которая пройдет по списку логов и вернет только те строки,
# где есть слово "Failed" (неудачная попытка входа).

#
# def find_hackers(logs):
#     return [log for log in logs if "Failed" in log]


# def find_hackers(logs):
#     result = []
#
#     for log in logs:
#         if "Failed" in log:
#             result.append(log)
#     return result

# Failed = [
#     "Accepted password for root",
#     "Failed password for admin",
#     "Connection closed by 192.168.1.5",
#     "Failed password for root"
# ]
#
# print(find_hackers(Failed))

# 2. В компании десятки серверов.
# У тестовых в названии есть слово test или dev, а у боевых - prod.
# Напишите функцию get_prod_servers(servers),
# которая выберет из общего списка только те серверы, в названии которых есть "prod".
#
# ["web-dev-01", "db-prod-01", "web-prod-02", "cache-test"]

# def get_prod_servers(servers):
#     return [server for server in servers if "prod" in server]

# def get_prod_servers(servers):
#     result = []
#
#     for server in servers:
#         if "prod" in server:
#             result.append(server)
#     return result
#
# lst_web =["web-dev-01", "db-prod-01", "web-prod-02", "cache-test"]
#
# print(get_prod_servers(lst_web))

# 3. Инженер проверяет историю команд стажера.
# Нужно написать функцию find_rm(history), которая найдет все команды, содержащие "rm ",
# чтобы убедиться, что стажер ничего не сломал.

# def find_rm(history):
#     return [rm for rm in history if "rm" in rm or rm.startswith("rm")]

# def find_rm(history):
#     result = []
#     for rm in history:
#         if "rm" in rm or rm.startswith("rm"):
#             result.append(rm)
#     return result
#
# cmd = ["ls -la", "cd /var/log", "rm temp.txt", "sudo apt update", "rm -rf /backup"]
#
# print(find_rm(cmd))


# 4. В конце месяца облачный провайдер
# присылает список списаний за каждый день (в долларах).
# Напишите функцию calculate_total_cost(daily_costs),
# которая посчитает общую сумму расходов за месяц.

# def calculate_total_cost(daily_costs):
#     return sum(daily_costs)

# def calculate_total_cost(daily_costs):
#     total = 0
#
#     for i in daily_costs:
#         total += i
#     return total
#
# #
# month = [12.5, 15.0, 10.2, 14.8, 20.0]
# print(calculate_total_cost(month))


# # 5. Дан список статусов контейнеров.
# # Напишите функцию count_exited(statuses),
# # которая посчитает, сколько контейнеров упали со статусом "Exited".
#
# # def count_exited(statuses):
# #     return len([status for status in statuses if "Exited" in status])
#
# def count_exited(statuses):
#     result = []
#
#     for status in statuses:
#         if "Exited" in status:
#             result.append(status)
#     return len(result)

# def count_exited(statuses):
#     count = 0
#     for status in statuses:
#         if "Exited" in status:
#             count += 1
#     return count
#
# exited = ["Running", "Running", "Exited", "Running", "Exited"]
#
# print(count_exited(exited))

# 6. Дан список названий баз данных.
# Напишите функцию generate_backup_names(databases),
# которая вернет новый список, где к каждой базе добавлено слово "_backup".

# def generate_backup_names(databases):
#     return [data + "_backup" for data in databases]
#
# def generate_backup_names(databases):
#     new_resultat = []
#
#     for data in databases:
#             new_resultat.append(data + "_backup")
#     return new_resultat
#
# lst = ["users", "orders", "products"]
#
# print(generate_backup_names(lst))

# 7. Дан список, где указан процент свободного места на дисках серверов: [80, 15, 45, 5].
# Напишите функцию check_storage(spaces),
# которая вернет True, если хотя бы на одном диске осталось меньше 10% свободного места (ранний выход).
# Иначе False.

# def check_storage(spaces):
#     for  percent in spaces:
#         if  percent < 10:
#             return True
#
#     return False
#
# disk = [80, 15, 45, 5]
# print(check_storage(disk))

# 8. На сервер пытается зайти IP-адрес "10.0.0.5".
# У вас есть список разрешенных адресов.
# Напишите функцию is_allowed(ip, whitelist), которая проверит, есть ли этот IP в разрешенном списке (через цикл for).

# Напишем программу, которая будет беспрерывно запрашивать
# ip-адреса и проверять есть ли они в разрешённом списке.
# Также прописать условия выхода из программы

# def is_allowed(ip, whitelist):
#     for i in whitelist:
#         if ip in i:
#             return "Такой IP в списке есть"
#
#     return "Этого IP нету в разрешенном списке"
#
#
# lst = ["192.168.1.1", "10.0.0.5", "172.16.0.2"]
#
# while True:
#     ip_users = input("Введите IP адрес/стоп - ")
#     if ip_users.lower() == "стоп":
#         break
#     print(is_allowed(ip_users, lst))

# 9. Чтобы развернуть приложение, на сервере должна быть установлена версия Python не ниже 3.8.
# Дан список версий на разных серверах: [3.9, 3.10, 3.6, 3.11].
# Напишите функцию get_ready_servers(versions), которая соберет в новый массив только версии >= 3.8.

# def get_ready_servers(versions):
#     new_versions = []
#     for version in versions:
#         parts = version.split(".")
#         first_number, second_number = int(parts[0]), int(parts[1])
#         if second_number >= 8 and first_number >= 3:
#             new_versions.append(version)
#     return new_versions
#
#
# python = ["3.9", "3.10", "3.6", "3.11"]
#
# print(get_ready_servers(python))

# 10. Пайплайн состоит из нескольких шагов:
# Сборка, Тестирование, Развертывание.
# Массив содержит статусы этих шагов.
# Напишите функцию is_pipeline_success(steps).
# Если в списке есть хотя бы один статус "failed", функция сразу возвращает "Деплой остановлен".
# Если цикл дошел до конца без ошибок - возвращает "Успешно завершено".
#

# def is_pipeline_success(steps):
#
#
# fail = ["success", "success", "failed", "pending"]

# Дан список оценок. Найдите средний балл.

# grades = [4, 5, 3, 4, 5]
#
# summa = sum(grades)
# count = len(grades)
#
# result = summa / count
#
# print(result)

# grades = [4, 5, 3, 4, 5]
#
# summa = 0
# count = 0
#
# for i in grades:
#     summa = summa + i
#     count = count + 1
#
# result = summa / count
#
# print(result)
#
# grades = [4, 5, 3, 4, 5]
# total = 0
# n = len(grades)
#
# for i in grades:
#     total += i / n
#
#
# print(total)

# Дан список: [10, 20, 30, 40, 50]
# Найдите среднее арифметическое.

# lst = [10, 20, 30, 40, 50]
#
# summa = 0
# count = 0
#
# for i in lst:
#     summa += i
#     count += 1
#
# result = summa / count
# print(result)

# Пользователь вводит 5 чисел через пробел
# Найдите их среднее арифметическое

# lst  = input("Введите 5 чисел через пробел  - ")
#
# new_lst = []
# for i in lst.split():
#     new_lst.append(i)
#
# summa = 0
# count = 0
#
# for e in new_lst:
#     summa += int(e)
#     count += 1
#
# result = summa / count
#
# print(result)

# lst  = input("Введите 5 чисел через пробел  - ")
#
# new_lst = [int(x) for x in lst.split()]
#
# result = sum(new_lst) / len(new_lst)
#
# print(result)

# Дан список: [4, 5, 3, 5, 5, 4, 4, 5]
# Найдите средний балл одним из способов:
# Способ 1 (ручной цикл)
# Способ 2 (sum/len)
# Способ 3 (list comprehension, если нужен новый список)

# lst = [4, 5, 3, 5, 5, 4, 4, 5]
#
# lst = [i for i in lst]
#
# result = sum(lst) / len(lst)
#
# print(result)

# lst = [4, 5, 3, 5, 5, 4, 4, 5]
#
# summa = 0
# count = 0
#
# for i in lst:
#     summa += i
#     count += 1
#
# result = round((summa / count), 2)
#
# print(result)

# lst = [4, 5, 3, 5, 5, 4, 4, 5]
#
# summa = sum(lst)
# count = len(lst)
#
# result = summa / count
#
# print(result)

# Дан список [3, 5, 4, 2, 5]
# Найдите среднее арифметическое
# ЗАПРЕЩЕНО использовать sum() и len()
# Используйте только цикл for и переменные

# grades = [3, 5, 4, 2, 5]
#
# summa = 0
# count = 0
#
# for i in grades:
#     summa += i
#     count += 1
#
# result = summa / count
#
# print(result)

# Дан список [100, 200, 300, 400, 500]
# Найдите среднее арифметическое
# ЗАПРЕЩЕНО использовать sum() и len()

# numbers = [100, 200, 300, 400, 500]
#
# summa = 0
# count = 0
#
# for i in numbers:
#     summa += i
#     count += 1
#
# result = summa / count
# print(result)

# Пользователь вводит числа, пока не введёт 0
# Найдите среднее всех введённых чисел (0 не учитывается)

# Пример:
# Ввод: 10, 20, 30, 0
# Среднее: (10+20+30) / 3 = 20


# summa = 0
# count = 0
#
# while True:
#     num = int(input("Введите число/ 0 для выхода - "))
#     if num == 0:
#         break
#
#     summa += num
#     count += 1
#
# if count > 0:
#     result = summa / count
#     print(result)
# else:
#     print("Чисел не введено")

# Дан список [15, 20, 25, 30, 35, 40]
# Найдите среднее арифметическое ТОЛЬКО чётных чисел
# (используйте цикл for и условие if)

# numbers = [15, 20, 25, 30, 35, 40]
#
# summa = 0
# count = 0
#
# for i in numbers:
#     if i % 2 == 0:
#         summa += i
#         count += 1
#
# result = summa / count
#
# print(result)

# Дан список [-5, 10, -3, 8, -2, 6]
# Найдите среднее арифметическое ТОЛЬКО положительных чисел

# lst = [-5, 10, -3, 8, -2, 6]
#
# summa = 0
# count = 0
#
# for i in lst:
#     if i > 0:
#         summa += i
#         count += 1
# result = summa / count
# print(result)

# Дан список словарей с оценками
# Найдите средний балл (простое среднее)

# grades = [
#     {"subject": "Math", "grade": 5},
#     {"subject": "English", "grade": 4},
#     {"subject": "History", "grade": 3}
# ]
#
# summa = 0
# count = 0
#
# for i in grades:
#     summa += i["grade"]
#     count += 1
#
# result = summa / count
# print(result)
#


# students = [
#     {"name": "Alice", "grade": 90},
#     {"name": "Bob", "grade": 80},
#     {"name": "Charlie", "grade": 85}
# ]
#
# grades = [i["grade"] for i in students]
# result = sum(grades) / len(grades)
#
# print(result)

# Дан список словарей с оценками и кредитами
# Найдите простое среднее (кредиты НЕ используем)

# grades = [
#     {"subject": "Math", "grade": 90, "credits": 4},
#     {"subject": "Physics", "grade": 80, "credits": 3},
#     {"subject": "Chemistry", "grade": 85, "credits": 4}
# ]
#
# summa = 0
# count = 0
#
# for i in grades:
#     summa += i["grade"]
#     count += 1
#
# result = summa / count
#
# print(result)

# Дан список результатов экзаменов
# Найдите средний балл

# exam_results = [
#     {"student": "Anna", "score": 88},
#     {"student": "Ivan", "score": 92},
#     {"student": "Maria", "score": 75},
#     {"student": "Peter", "score": 100}
# ]
#
# summa = 0
# count = 0
#
# for i in exam_results:
#     summa += i["score"]
#     count += 1
#
# result = summa / count
#
# print(result)

# Найдите средний балл ВСЕХ студентов
# (по всем университетам, факультетам, программам)
# Структура:
# data["universities"][...]["students"][...]["grades"][...]["grade"]
# Нужно:
# 1. Загрузить JSON из файла
# 2. Пройти по всем студентам
# 3. Собрать ВСЕ оценки (grade) из всех студентов

# import json
#
# from tutorial import student
#
# with open("universities_big.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#
# summa = 0
# count = 0
#
# for univ in data["universities"]:
#     for stud in univ["students"]:
#         for grade in stud["grades"]:
#             summa += grade["grade"]
#             count += 1
# result = summa / count
# print(result)

# Дан список словарей с course_id и grade
# Найдите средний балл, округлите до 2 знаков

# grades = [
#     {"course_id": 101, "grade": 85},
#     {"course_id": 102, "grade": 90},
#     {"course_id": 103, "grade": 78}
# ]
#
# summa = 0
# count = 0
#
# for i in grades:
#     summa += i["grade"]
#     count += 1
#
# result = round((summa / count), 2)
#
# print(result)

# Дан словарь студента с оценками (список чисел)
# Найдите средний балл студента

# student = {
#     "name": "John",
#     "grades": [85, 90, 78, 92, 88]
# }
#
# summa = 0
# count = 0
#
# for i in student["grades"]:
#     summa += i
#     count += 1
#
# result = summa / count
#
# print(result)

# Дан словарь студента с оценками (список словарей)
# Найдите средний балл студента

# student = {
#     "name": "Elena",
#     "grades": [
#         {"course": "Math", "grade": 95},
#         {"course": "Physics", "grade": 87},
#         {"course": "Chemistry", "grade": 91}
#     ]
# }
#
# summa = 0
# count = 0
#
# for stud in student["grades"]:
#         summa += stud["grade"]
#         count += 1
#
# result = summa / count
#
# print(result)

# Дан словарь студента с результатами экзаменов
# Найдите средний балл
#
# student = {
#     "name": "Dmitry",
#     "exams": [
#         {"exam_id": 1, "score": 76},
#         {"exam_id": 2, "score": 84},
#         {"exam_id": 3, "score": 92},
#         {"exam_id": 4, "score": 88}
#     ]
# }
#
# summa = 0
# count = 0
#
# for exam in student["exams"]:
#     summa += exam["score"]
#     count += 1
#
# result = summa / count
#
# print(result)

# Дан словарь студента с оценками за три семестра
# Найдите средний балл за ВСЕ семестры
#
# student = {
#     "name": "Olga",
#     "semester_1": [88, 92, 85],
#     "semester_2": [90, 87, 93],
#     "semester_3": [86, 89, 91]
# }
#
# summa = 0
# count = 0
#
# for semester in student["semester_1"]:
#     summa += semester
#     count += 1
#
# for semester1 in student["semester_2"]:
#     summa += semester1
#     count += 1
#
# for semester2 in student["semester_3"]:
#     summa += semester2
#     count += 1
#
# result = summa / count
# print(result)

# Дан словарь студента с оценками (ключ = предмет, значение = оценка)
# Найдите средний балл

# student = {
#     "name": "Maxim",
#     "grades": {
#         "Math": 95,
#         "Physics": 88,
#         "English": 92,
#         "History": 85
#     }
# }
# summa = 0
# count = 0
#
# for i in student["grades"].values():
#     summa += i
#     count += 1
#
# result = summa / count
#
# print(result)


# Дан список студентов (у каждого только одна оценка)
# Верните словарь {имя: средний_балл} (у каждого только одна оценка)

# students = [
#     {"name": "Anna", "grade": 90},
#     {"name": "Bob", "grade": 85},
#     {"name": "Clara", "grade": 88}
# ]
#
# new_dict = {}
# for i in students:
#     student_name = i["name"]
#     student_grade = i["grade"]
#     new_dict[student_name] = student_grade
# print(new_dict)

# Нужно получить:
# {"Anna": 87.67, "Bob": 80.67} (среднее арифметическое).

# students = [
#     {"name": "Anna", "grades": [90, 85, 88]},
#     {"name": "Bob", "grades": [70, 92, 80]},
# ]
#
# new_dict = {}
#
# for i in students:
#     student_name = i["name"]
#     student_grade = i["grades"]
#     student_average =round(sum(student_grade) / len(student_grade),2)
#     new_dict[student_name] = student_average
# print(new_dict)

# Дан список серверов. У каждого — имя и список загрузки CPU по минутам.
# Нужно вывести имена серверов, у которых средняя загрузка выше 85.

# servers = [
#     {"name": "web-1", "cpu": [90, 85, 88, 92]},
#     {"name": "web-2", "cpu": [45, 50, 48, 52]},
#     {"name": "web-3", "cpu": [95, 97, 93, 96]},
# ]
#
# lst = []
# for  i in servers:
#     server_name = i["name"]
#     server_cpu = i["cpu"]
#     server_average = round(sum(server_cpu) / len(server_cpu),2)
#     if server_average > 85:
#         lst.append(server_name)
# print(lst)

# У тебя есть JSON (я его сократил, но структура та же, что и в твоём файле).
# Нужно найти средний балл студента с student_id = 7 по всем его оценкам (поле grades).

# import json
#
# data_str = '''
# {
#   "students": [
#     {
#       "student_id": 7,
#       "name": "Тимур Иванов",
#       "grades": [
#         {"course_id": 9038, "grade": 82},
#         {"course_id": 9018, "grade": 75},
#         {"course_id": 9024, "grade": 61}
#       ]
#     }
#   ]
# }
# '''
#
# data = json.loads(data_str)
#
# summa = 0
# count = 0
#
# for student in data["students"]:
#     if student["student_id"] == 7:
#         for grade in student["grades"]:
#             summa += grade["grade"]
#             count += 1
#
# result = round((summa / count), 2)
#
# print(result)

# Дан тот же JSON (со студентами и их оценками).
# Нужно для каждого студента посчитать его средний балл и вывести в виде:
# Тимур Иванов: 72.67
# Павел Федоров: 77.00
# Следующий шаг (по желанию)
# Можешь усложнить себе задачу:
# Добавить проверку, что список grades не пустой (чтобы не было деления на ноль).
# Сохранить результаты в словарь: {student_id: average, ...}.
# Вывести студентов, у которых средний балл выше 80.
# Если хочешь — попробуй один из вариантов. Если нет — просто прими победу.
# Ты сегодня решил задачу, с которой многие спотыкаются.


# import json
#
# from tutorial import student

# data_str = '''
# {
#   "students": [
#     {
#       "student_id": 7,
#       "name": "Тимур Иванов",
#       "grades": [
#         {"course_id": 9038, "grade": 82},
#         {"course_id": 9018, "grade": 75},
#         {"course_id": 9024, "grade": 61}
#       ]
#     },
#     {
#       "student_id": 12,
#       "name": "Павел Федоров",
#       "grades": [
#         {"course_id": 9040, "grade": 71},
#         {"course_id": 9035, "grade": 83}
#       ]
#     }
#   ]
# }
# '''
# data = json.loads(data_str)
#
# averages = {}
# for student in data["students"]:
#
#
#     if len(student["grades"]) == 0:
#         print(f"{student['name']}: нет оценок")
#         continue
#
#     summa = 0
#     count = 0
#
#     for grade in student["grades"]:
#         summa += grade["grade"]
#         count += 1
#
#     result = round((summa / count), 2)
#     if result > 60:
#         averages[student["name"]] = result
#
# print(averages)

# summa = 0
# count = 0
#
# summa1 = 0
# count1 = 0
#
# for student in data["students"]:
#     if student["student_id"] == 7:
#         for grade in student["grades"]:
#             summa += grade["grade"]
#             count += 1
# result = round((summa / count), 2)
# for students in data["students"]:
#     if students["student_id"] == 12:
#         for grades in students["grades"]:
#             summa1 += grades["grade"]
#             count1 += 1
# result1 = round((summa1 / count1), 2)
#
# print(result)
# print(result1)

# Задача
# У тебя есть список серверов. Каждый сервер — это словарь с полями:
# "name" — имя сервера
# "cpu" — список загрузки CPU по минутам (числа)
# "failed_checks" — количество неудачных проверок (целое число)
# Нужно:
# Посчитать среднюю загрузку CPU для каждого сервера.
# Если средняя загрузка > 75 или failed_checks > 3 — добавить сервер в список «проблемных».
# Для проблемных серверов вывести строку:
# {имя сервера}: средняя нагрузка {значение}, ошибок {failed_checks}

# servers = [
#     {"name": "web-1", "cpu": [90, 85, 88, 92], "failed_checks": 4},
#     {"name": "web-2", "cpu": [45, 50, 48, 52], "failed_checks": 1},
#     {"name": "db-1", "cpu": [95, 97, 93, 96], "failed_checks": 0},
#     {"name": "cache-1", "cpu": [30, 35, 28, 32], "failed_checks": 5},
# ]
#
#
# problematic = []
#
#
# for server in servers:
#     server_name = server["name"]
#     server_cpu = server["cpu"]
#     average = sum(server_cpu) / len(server_cpu)
#     if average > 75 or server["failed_checks"] > 3:
#         line = f"{server_name}: средняя нагрузка {round(average, 2)}, ошибок {server['failed_checks']}"
#         problematic.append(line)
# for item in problematic:
#     print(item)

import random

# colors = ["red", "green", "blue"]
# print(random.choice(colors))

# servers = ["web-1", "web-2", "db-1", "cache-1"]
# print(f"Для проверки выбран сервер: {random.choice(servers)}")

# servers = ["web-1", "web-2", "db-1", "cache-1"]
# print(f"Для нагрузочного тестирования выбран сервер: {random.choice(servers)}")

# Пример для твоей задачи 2
# Тебе нужно:
# Случайное число от 1 до 5
# Сохранить в переменную
# Вывести сообщение с этим числом

# delay = random.randint(1,5)
# print(f"Задержка перед проверкой: {delay} секунд")


# Выбрать случайный сервер
# Выбрать случайное действие
# Вывести в формате:

# servers = ["web-1", "web-2", "db-1", "cache-1"]
# actions = ["проверить CPU", "проверить память", "проверить диск", "перезагрузить"]
#
# server= random.choice(servers)
# action = random.choice(actions)
#
# print(f"На сервере {server} выполняем действие: {action}")

# Переходим к задаче 4 (последняя)
# Условие:
# Выбрать случайный порт от 8000 до 8999 (включительно) и вывести:
# Тестовый сервер запущен на порту: 8473

port = random.randint(8000, 8999)
print(f"Тестовый сервер запущен на порту: {port}")













