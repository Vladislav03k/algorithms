'''
 В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
 Примечание: 8 разных ответов.
'''
main_range = list(range(2, 100))
print(main_range)

import cProfile
# divisor_range = list(range(2, 10))
# print(divisor_range)

def divisor(list):
    div_2 = 0
    div_3 = 0
    div_4 = 0
    div_5 = 0
    div_6 = 0
    div_7 = 0
    div_8 = 0
    div_9 = 0
    for el in list:
        if el % 2 == 0:
            div_2 += 1
        if el % 3 == 0:
            div_3 += 1
        if el % 4 == 0:
            div_4 += 1
        if el % 5 == 0:
            div_5 += 1
        if el % 6 == 0:
            div_6 += 1
        if el % 7 == 0:
            div_7 += 1
        if el % 8 == 0:
            div_8 += 1
        if el % 9 == 0:
            div_9 += 1
        return div_2, div_3, div_4, div_5, div_6, div_7, div_8, div_9

# div_2 = 0
# div_3 = 0
# div_4 = 0
# div_5 = 0
# div_6 = 0
# div_7 = 0
# div_8 = 0
# div_9 = 0
#
# for el in main_range:
#     if el % 2 == 0:
#         div_2 += 1
#     if el % 3 == 0:
#         div_3 += 1
#     if el % 4 == 0:
#         div_4 += 1
#     if el % 5 == 0:
#         div_5 += 1
#     if el % 6 == 0:
#         div_6 += 1
#     if el % 7 == 0:
#         div_7 += 1
#     if el % 8 == 0:
#         div_8 += 1
#     if el % 9 == 0:
#         div_9 += 1
#
# print(div_2, div_3, div_4, div_5, div_6, div_7, div_8, div_9)

# 1000 loops, best of 5: 6.5 nsec per loop

cProfile.run(divisor(main_range))