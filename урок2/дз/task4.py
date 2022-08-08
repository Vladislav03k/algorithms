'''
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
'''
# summ = 1
# n = int(input('Введите количество эллементов: '))
# count = 0
# i = 1
# while count != n:
#     i /= -2
#     print(i)
#     summ += i
#     count += 1
# print(summ)

def summ(n):
    summa = 1
    count = 0
    i = 1
    while count != n:
        i /= -2
        summa += i
        count += 1
    return summa

n = int(input('Введите количество эллементов: '))
print(summ(n))