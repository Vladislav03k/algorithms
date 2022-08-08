'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
'''
def reverse(string):
    new_num = ''
    ind = len(string)
    for i in range(ind - 1, -1, -1):
        new_num += string[i]
    return new_num

num = str(input('Введите число: '))
print(reverse(num))