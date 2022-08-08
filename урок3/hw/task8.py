'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''
import random

matrix = [[random.randint(0,10) for _ in range(5)] for _ in range(7)]
for line in matrix:
    for item in line:
        print(f'{item:<4}', end=' ')
    print()
