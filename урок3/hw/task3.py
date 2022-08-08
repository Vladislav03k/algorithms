'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
'''
import random

el_max = float('-inf')
el_min = float('inf')
idx_max = 0
idx_min = 0

main_range = [random.randint(0,100) for _ in range(10)]
print(main_range)

for el in main_range:
    if el >= el_max:
        el_max = el
        idx_max = main_range.index(el_max)
    elif el <= el_min:
        el_min = el
        idx_min = main_range.index(el_min)

print(el_min, el_max, idx_min, idx_max)

main_range[idx_min] = el_max
main_range[idx_max] = el_min
print(main_range)

