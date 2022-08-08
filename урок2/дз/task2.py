'''
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''
num = str(input('Введите натуральное число: '))
evenel = 0
unevenel = 0
even = ''
uneven = ''
for i in num:
    if int(i) % 2 == 0 or int(i) == 0:
        evenel += 1
        even = even + ' ' +str(i)
    else:
        unevenel += 1
        uneven = uneven + ' ' + str(i)
print(f'В числе {num} {evenel} четных цифр ({even}) и {unevenel} нечетных цифр ({uneven})')