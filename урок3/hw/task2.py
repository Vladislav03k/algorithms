'''
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа.
'''
import random

main_range = [random.randint(0, 100) for _ in range(10)]
print(main_range)

idx_range = []

for el in main_range[:]:
    if el % 2 == 0:
        idx_range.append(main_range.index(el))

print(idx_range)