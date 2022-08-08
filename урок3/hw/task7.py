'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''
import random

r = [random.randint(-100,100) for _ in range(10)]
print(r)

el_min = float('inf')
idx_min = 0

for el in r:
    if el <= el_min:
        el_min = el
        idx_min = r.index(el_min)

print(idx_min, el_min)
fst_min_el = el_min

el_min = float('inf')
r.pop(idx_min)
print(r)
for el in r:
    if el <= el_min:
        el_min = el
        idx_min = r.index(el_min)

print(idx_min, el_min)
snd_el_min = el_min

print(fst_min_el, snd_el_min)
