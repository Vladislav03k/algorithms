'''
Определить, какое число в массиве встречается чаще всего.
'''
import random

main_range = [random.randint(0, 10) for _ in range(10)]
print(main_range)

max_tuple = (0, main_range[0])
for el in main_range:
    count = main_range.count(el)
    if count > max_tuple[0]:
        max_tuple = (count, el)

print(f'Повторяется раз: {max_tuple[0]} число: {max_tuple[1]}')
# same_el = list(set(main_range))
#
# print(same_el)
#
# prev_el = 0
#
# for el in main_range:
#     if el in same_el:
#         print(el)