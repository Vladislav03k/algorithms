'''
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно
'''

import random
import string

question = input(f'Выберите вариант действия:\n'
                 '1 - Диапазон целочисленных значений\n'
                 '2 - Диапазон числе с плавающей точкой\n'
                 '3 - Диапазон буквенных значений\n'
                 'Ваш выбор: ')

if question == '1':
    start = int(input('Введите начало диапазона: '))
    stop = int(input('Введите конец диапазона: '))
    c = random.randint(start, stop)
    print(c)
elif question == '2':
    start = float(input('Введите начало диапазона: '))
    stop = float(input('Введите конец диапазона: '))
    c = random.uniform(start, stop)
    print(c)
elif question == '3':
    start = input('Введите букву начало диапазона: ')
    stop = input('Введите букву конец диапазона: ')
    c = random.choice(string.ascii_lowercase)
    print(c)
else:
    print('Неверно выбранный вариант')