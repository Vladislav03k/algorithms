import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

num = int(input('Введите число которое хотите вставить: '))
pos = int(input('Введите позицию на которую необходимо вставить число: '))

# array.append(None)
# i = len(array) - 1
#
# while i > pos:
#     array[i], array[i - 1] = array[i - 1], array[i]
#     i -= 1

# array.insert(num, pos)

array_new = array[:pos] + [num] + array[pos:]

array[pos] = num
print(array)