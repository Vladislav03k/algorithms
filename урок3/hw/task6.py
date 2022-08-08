'''
 В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
 Сами минимальный и максимальный элементы в сумму не включать.
'''
import random

r = [random.randint(-100,100) for _ in range(10)]
print(r)

el_max = float('-inf')
el_min = float('inf')
idx_max = 0
idx_min = 0

for el in r:
    if el >= el_max:
        el_max = el
        idx_max = r.index(el_max)
    elif el <= el_min:
        el_min = el
        idx_min = r.index(el_min)

print(el_min, el_max, idx_min, idx_max)
new_r = r[:]
new_r.pop(idx_max)
new_r.pop(idx_min)
print(new_r)

sum_r = 0

for el in new_r:
    sum_r += el

print(sum_r)
