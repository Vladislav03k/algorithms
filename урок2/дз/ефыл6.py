def find_num(count, num):
    count_i = 0
    num_count = 0
    big_str = ''
    while count != count_i:
        num_pers = str(input('Введите число: '))
        count_i += 1
        big_str += num_pers
    for i in big_str:
        if i == str(num):
            num_count += 1
    return num_count

count = int(input('Введите количество чисел вводимых пользователем: '))
num = int(input('Введиете цифру которую надо найти: '))
print(find_num(count, num))

