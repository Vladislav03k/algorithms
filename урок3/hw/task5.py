'''
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
'''
import random

r = [random.randint(-10,10) for _ in range(10)]
print(r)

# min_els = []
min_el = float('-inf')
# max_min_el = 0
for i, item in enumerate(r):
    if min_el < item < 0:
        min_el = item
        min_idx = i

print(min_idx, min_el)

# print(min_els)
#
# for el in min_els:
#     if el < min_el:
#         min_el = el
#
# print(min_el)
#
# for el in min_els:
#     if el > min_el:
#         max_min_el = el
#
# print(max_min_el)
